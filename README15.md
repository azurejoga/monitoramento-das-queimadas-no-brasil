# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44289c29-1b8b-3ef8-9112-40829e66b123 | -10.55012 | -52.03416 | 2025-07-01 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45438a0b-2c50-388f-a20f-f3d8e518b100 | -10.08879 | -52.73907 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 258a60ef-95ca-33e0-9f26-c8c928baf835 | -10.07576 | -52.74102 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24a64ae7-1ec3-3019-9912-138e4e1f9949 | -10.86996 | -53.76235 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88e36ccd-2a84-363f-b2b4-f0c320926f2f | -10.87526 | -56.44366 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 55558daf-7edd-33c3-b162-d2f44d43443b | -10.87775 | -56.43665 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d7fbbdc-4b99-3da1-89ef-5ad4e39c02a8 | -12.01055 | -62.82933 | 2025-07-01 05:14:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40671f13-08ed-3bf4-abef-b8ac08071659 | -9.71688 | -56.18276 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9183f3a8-3d55-3928-bd79-0050f7ef9f47 | -10.29627 | -57.13499 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ba23d2-8f05-3e39-b284-a80f7ee2fb8c | -9.35576 | -58.85475 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a59e329b-a254-39fb-b3ce-9156bdc75e58 | -9.08216 | -59.48796 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c64d9c4-ed6f-3993-835d-cb5ddc9d1afe | -9.08392 | -59.47703 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 258d43cc-ce08-3e19-a992-62903eb4521f | -10.88558 | -56.44529 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 382cd81c-88a0-3a29-be1c-21c7bccad3e0 | -11.12839 | -55.44693 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee88aded-3d34-38ac-b73d-a3ff33f82e42 | -9.25066 | -58.74731 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d46c626-9021-3a9b-88b0-20fd3dde8ed4 | -9.0879 | -59.47393 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8021f2fb-41a5-3b3b-92b7-148d524e87b0 | -10.87786 | -53.76345 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b45e0e2-9a69-3326-bf67-5be7b584a849 | -12.63424 | -54.21717 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d984c86e-5dc3-39a5-b7c6-16a79c29cedb | -9.24393 | -58.76794 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7869606-2642-3351-b354-ad3cf1318ed4 | -10.877 | -56.45557 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27a1b6ac-130d-3aa3-8ecb-718c2002d07d | -10.12612 | -57.77356 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4186dad-9cb4-3b64-b0a0-285452c7a22e | -9.23844 | -58.7381 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 052644d5-65af-3c53-b4e8-ef20478e2bfb | -9.11408 | -59.05292 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df8ed69f-0c67-3319-b6fd-e954e117a86e | -11.58343 | -52.11787 | 2025-07-01 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b98234-4e57-3e9a-958b-e59fa1f0958e | -11.12417 | -55.45056 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81143242-d91b-35c6-a512-df501eec7272 | -10.08408 | -52.74225 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| afb090d1-6a38-318f-95e9-85c0cf1819b8 | -12.82762 | -47.36773 | 2025-07-01 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f65628ff-04cf-3330-a9f6-aa967f8c7ad8 | -10.02548 | -54.3216 | 2025-07-01 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15ad9360-d01a-3e92-b8c2-c5d29f2111e6 | -9.08731 | -59.47759 | 2025-07-01 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e991eafc-3300-3b82-9595-fb6a7fa2dfa9 | -12.02394 | -47.76889 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 667cc9ae-b650-3b10-8ce5-f243734840d5 | -12.10556 | -54.56801 | 2025-07-01 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8480c57a-3077-3575-a26d-df2288504734 | -12.01796 | -47.76813 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fda1e846-f4dc-3370-9b01-ef218a46bcc7 | -10.87928 | -53.75335 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c3b724-6fbb-3282-9e4e-259e663f3e4d | -11.59677 | -65.14551 | 2025-07-01 05:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07bc21ff-b45f-3e61-b725-2d85ea730eb4 | -11.20207 | -55.91298 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba1cbf5f-85e4-3041-aaf8-946e79b22286 | -10.28232 | -52.83052 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f8ed345-dfd1-3e43-a1c2-d81190f8388f | -10.87717 | -56.44043 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4928d78c-8042-3594-9cff-54f6b1c3f1dc | -9.70254 | -56.18438 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f75d432-feb5-32dc-8abb-1999cb92c144 | -10.5546 | -52.03367 | 2025-07-01 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b90151-790e-38d5-ba5e-8d289d48af58 | -9.24732 | -58.74677 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ecbd729-8409-39db-9b39-0d4b7529b1ef | -10.87413 | -56.45124 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ec0287-0fb1-3ceb-99b1-8eaf6a38c68e | -11.57815 | -48.14289 | 2025-07-01 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aaf91cd-9c58-353b-b264-c892ea97ee11 | -10.67821 | -49.1534 | 2025-07-01 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8572b653-e899-3a58-8f69-f0cb7edbc4af | -10.3013 | -57.12471 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d32b164b-6ddc-375e-a1d3-0b7cd5fc0153 | -9.23618 | -58.75222 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe5407f6-7f20-362d-8525-0fe89c66a689 | -14.20029 | -45.51965 | 2025-07-01 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da1cbebf-ef30-3ec9-b43a-6b16b8cc9e58 | -11.57533 | -54.56517 | 2025-07-01 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d29e8ae-ebfb-3840-9091-da848c778e5c | -13.01253 | -53.42302 | 2025-07-01 05:14:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d78ab82f-d277-3ce9-aa9c-048125bc4d86 | -10.93436 | -55.32666 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0af63e6-1268-391a-a4e8-f3bf96594598 | -10.07832 | -52.75296 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8dba39b-49c5-3fa2-8ee9-41bebe0d00b8 | -9.97216 | -48.24442 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c83d57d5-0878-3e52-a366-704fee232b06 | -10.30636 | -57.13656 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 155e2f43-e918-3e2e-879a-d087eded0480 | -12.28612 | -50.10783 | 2025-07-01 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1029dab9-2147-3b60-a56a-8dc1ba3567b6 | -10.87355 | -53.73687 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53d5198d-3f88-3d77-b57c-0b01c59009ad | -9.70999 | -56.1817 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a279a6f4-9a1d-316d-ada1-0c350cb1dade | -10.29683 | -57.13139 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adc7e483-e399-3152-baa5-34d94414acef | -11.07584 | -55.37917 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47147a61-b6fe-3d32-9d10-2a228e2e8255 | -10.87757 | -56.45178 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 574d8b88-d803-3e3c-ba8e-b544e926887b | -10.13097 | -57.78143 | 2025-07-01 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7abd864-4c13-3c20-a097-f3c740b0d789 | -12.82141 | -47.36707 | 2025-07-01 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df5ba06a-a5e6-3765-abff-963f3bed73c1 | -10.13085 | -52.3493 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 601eb4eb-10fb-3825-97e0-1fbee52230a4 | -10.12714 | -52.34463 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8d1b9ec-521a-35aa-be6c-817ba6b576e2 | -10.87755 | -49.54631 | 2025-07-01 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d966709d-0f15-3e24-9b7a-6917f235318f | -9.23008 | -58.7476 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5efcfec6-cdda-34d3-9047-6825384947e8 | -12.28498 | -50.0997 | 2025-07-01 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4da6b4e9-5f80-3baf-a32d-8557f8645a8f | -10.30019 | -57.13192 | 2025-07-01 05:14:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a44c2830-9c34-34c3-956a-88b89ae99d9b | -9.23511 | -58.73756 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a76b8de2-556c-37c2-ac93-b131ef436c6e | -11.20499 | -55.91754 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 661326e3-3fbb-3d51-9a12-623e7cd41679 | -9.24896 | -58.75789 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012fd8d6-b010-3e32-a63f-7a8ecd1e72df | -11.01757 | -56.2621 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166ad5ff-4faf-32d1-91e9-d092f3352e4d | -10.87373 | -56.43988 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 221d770e-8149-3fec-985a-11aa40e7122d | -9.97464 | -48.2459 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a24e9b0e-50cf-37b1-8749-8301dc919d82 | -10.06905 | -49.65989 | 2025-07-01 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e333459-00ce-3cb2-9789-054d1bbb3f0a | -9.35967 | -58.85175 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4492e562-6103-3984-9e7b-2ed99374299b | -12.62962 | -54.22162 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5192ad99-65c3-3bde-8299-631428d829fb | -11.83093 | -62.77311 | 2025-07-01 05:14:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf546bec-eaa1-3f13-9872-cac30ed2bfa9 | -11.02157 | -56.23518 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b85fae7-78cf-3108-9846-246ea97813ed | -9.97265 | -48.2405 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f6241ab1-3b9b-3979-b2de-7a6227b76d90 | -10.1223 | -52.34806 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34438ac0-d164-397e-b681-22a8e0fd4ba7 | -9.97781 | -48.24516 | 2025-07-01 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb18d1ee-61c6-32ae-8beb-18717464b9eb | -12.28574 | -50.11092 | 2025-07-01 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18bab42d-08b7-3ef3-a7e0-1fa46da39d4d | -14.20731 | -45.52053 | 2025-07-01 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d4f4c0c-8691-38b6-bcb1-221794b4a570 | -12.10487 | -54.5728 | 2025-07-01 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e97edb9e-5bd4-3fdf-a975-b520c0b394c3 | -9.23901 | -58.73458 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1e053f7-dfe7-3b36-9114-3633fe666a01 | -10.87983 | -56.43663 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da4c4fd-365c-3e37-89c0-85ea4afe3dab | -9.23341 | -58.74814 | 2025-07-01 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffc68949-e711-390f-a514-abd301220c94 | -12.28338 | -50.11207 | 2025-07-01 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fee6a718-2e82-3931-b089-22be03cdc746 | -12.01687 | -47.7772 | 2025-07-01 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9aec8255-0d81-306e-a48e-453ecbfc01f8 | -11.02797 | -56.26377 | 2025-07-01 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a08dfb5e-71b3-3364-ad82-d9f7673081b3 | -10.62397 | -51.78834 | 2025-07-01 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d28d2d2-6347-3593-ab26-ddd81d4cb45d | -14.44245 | -48.87012 | 2025-07-01 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7053a1bc-4538-3431-81e1-f7a19decee5c | -11.57306 | -48.14224 | 2025-07-01 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a311c0e-7c62-382d-b658-d80e2fb911ef | -10.93558 | -55.32529 | 2025-07-01 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1844d9f8-2df3-3448-b081-76cb37f10cb1 | -9.69968 | -56.18007 | 2025-07-01 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a585e902-5feb-38da-b489-b12d37ae5c1c | -10.02171 | -54.32103 | 2025-07-01 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fe142a5-060f-3644-9650-e35f57c3c589 | -12.6257 | -54.22104 | 2025-07-01 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d36cce09-a1c8-334d-8f46-7661af688b23 | -10.12658 | -52.34869 | 2025-07-01 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03e75bad-7924-38b7-82cb-732ac1967d38 | -10.87714 | -53.7685 | 2025-07-01 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 324c7784-0762-33b5-a397-6b29ad666ad9 | -11.57899 | -52.11723 | 2025-07-01 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 106aee74-5578-3445-b8c0-f30197729a2f | -9.65612 | -50.74129 | 2025-07-01 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README16.md)
