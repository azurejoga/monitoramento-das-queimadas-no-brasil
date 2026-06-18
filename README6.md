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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 559f07c5-d648-3c96-9e09-1592d027e4e3 | -10.56307 | -46.22963 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 350ff3e9-35c5-3c0a-8ec4-574dd1d4f684 | -11.81182 | -47.34206 | 2026-06-18 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce1a202-b1ed-34a3-b21e-e9691fd7df36 | -10.55711 | -46.23111 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dfe982a-c378-3636-8b12-e186743678e4 | -8.83943 | -44.80302 | 2026-06-18 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 690b406e-6333-3aa0-b6f9-f112b87b036d | -8.60981 | -45.99372 | 2026-06-18 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a09d66d-f217-3ec3-aed1-ff1eee6ff33c | -11.9886 | -38.96282 | 2026-06-18 04:00:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27e4952b-b142-3fcd-9f0c-cc30ed66a13a | -8.79634 | -46.63563 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a943fb38-d3ac-3691-9e9b-3de03ee3f9ba | -10.65023 | -49.20002 | 2026-06-18 04:00:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f0c7c37-67c5-397b-b6a4-22aec723d08f | -12.76495 | -44.5356 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a1f4042-12e6-3a76-a0fc-be8eee6304b8 | -13.81299 | -43.65014 | 2026-06-18 04:00:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2671126a-d60a-3f4a-a2a8-41390ec1d647 | -12.84591 | -44.36972 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59166757-55e5-3fa7-bdf9-0596caa55c09 | -11.24661 | -46.62244 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1f3b23b-d36d-3336-ab43-fd6e4456a869 | -11.81052 | -52.52597 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36d27d4b-f2c9-383d-aa27-384fc01ec97a | -12.20547 | -52.78016 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9824f2ad-4510-3c24-a0a3-dd37f627372e | -10.55259 | -46.23026 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5d1e5c-a2ac-34a0-ac01-c387f27376a2 | -9.59434 | -48.19074 | 2026-06-18 04:00:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5711f96-57f2-3fa3-92aa-7e0c96679057 | -9.77758 | -48.97305 | 2026-06-18 04:00:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2275147-1f4c-3aae-91dc-fc271602b344 | -12.20673 | -52.77422 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 794deb4e-f325-31f4-8022-d1ed5c1b7838 | -10.05031 | -48.09528 | 2026-06-18 04:00:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a50c6fe2-0f82-3946-95e2-1c3c80a2fa62 | -12.08922 | -44.97359 | 2026-06-18 04:00:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0e6d5037-e021-3022-99df-c068728c8b4b | -14.06129 | -44.48012 | 2026-06-18 04:00:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c53ff646-a4aa-302a-a78d-5fcc17c894cd | -12.09865 | -43.65161 | 2026-06-18 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 081d5022-461b-3620-97a2-05eeea729c95 | -10.74627 | -48.54023 | 2026-06-18 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b05bfaf8-110c-36f3-ac50-649e3fdbb439 | -11.25026 | -46.62608 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d7aa15d-b94d-3540-807d-75f4eb255366 | -10.86572 | -43.96827 | 2026-06-18 04:00:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a492f8d-eedb-3fb1-80b3-510d38ffcf7b | -9.21454 | -47.9345 | 2026-06-18 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 90f3d6ef-0f9f-3a22-8ca1-3b634f4c4f42 | -14.71648 | -42.94529 | 2026-06-18 04:00:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ec2e62af-80ec-31e3-8be4-1fc718e26d0e | -12.84388 | -44.36537 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7645c1ea-b262-30eb-a0ed-9fb4add41373 | -8.80208 | -46.6312 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd399691-ab30-3fea-8eed-58a4be1f6fc9 | -8.80305 | -46.62584 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9514c89e-b622-31bf-8e58-667c93467706 | -12.77186 | -44.54213 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74dee729-ae62-3f93-8dc3-c76c8ea1a32c | -9.21512 | -47.93136 | 2026-06-18 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ec5af4f1-8e20-320c-a3ae-47db597060f5 | -10.55318 | -46.23257 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2f9c4af-a565-3bc0-aeb8-77ba61320aaf | -10.98209 | -47.74548 | 2026-06-18 04:00:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc8dffcc-be74-3b4b-ba4b-ab42e50084fc | -13.94646 | -46.02911 | 2026-06-18 04:00:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00e04928-73a1-3e16-824f-c119a77a1ba0 | -10.98709 | -47.74628 | 2026-06-18 04:00:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4f28eb2b-f696-3103-ab56-25f7dcc46c60 | -11.20682 | -46.58047 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 956da8ce-a0b2-3487-9522-f4288d2650f2 | -12.06859 | -47.55608 | 2026-06-18 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc824f4-7471-3dcb-8d51-66c1a69bb23c | -8.987 | -47.03203 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7369e77e-e166-3219-b837-468d00f0e353 | -9.53679 | -40.34219 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 057b72a7-049a-352d-aed8-39aa9332d842 | -8.97377 | -47.97937 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54e28111-8f2d-3b12-a8de-d631eb84980f | -8.91003 | -46.97056 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 201276ca-686d-390f-a51e-f1d01ebb1c4d | -10.91052 | -46.34194 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a20b6db6-e8ab-39c3-bf44-7910dcc6dfbc | -13.94718 | -46.02509 | 2026-06-18 04:00:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15a73d2b-90f7-3926-aad6-7f45e3342ec8 | -10.9771 | -47.74466 | 2026-06-18 04:00:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c604c17-09ad-3970-850b-238e72105790 | -11.63237 | -38.93818 | 2026-06-18 04:00:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6543d49f-95d8-3147-96f2-bf3183d09374 | -12.0891 | -44.97314 | 2026-06-18 04:00:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7437fd7e-e399-33b8-a66e-c1414d596369 | -12.77098 | -44.54716 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4699ca6d-40f9-3850-bbe4-3e34040f38cc | -12.8421 | -44.37529 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7fff315-669f-3fab-8263-bfa59483e906 | -12.83733 | -44.3733 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 432be25e-5d95-3122-9671-0bd4a7015a99 | -10.55855 | -46.22877 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8d07726-7702-34f9-80b8-3d0999f27950 | -8.93696 | -48.00256 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70077952-1f53-3f53-9c7a-a1b21bb81baf | -12.84119 | -44.374 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c4929ef6-f08b-3eff-9baa-7e4925c00b90 | -13.75687 | -43.27596 | 2026-06-18 04:00:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5e48e90-508a-37e0-93f1-25355de1db52 | -9.21049 | -47.92736 | 2026-06-18 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fab53ba0-67b1-3ffe-8a47-8ccf8160fce1 | -11.24933 | -46.63107 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e3e7263-ec7f-3163-ac06-d9ad19354f47 | -9.21569 | -47.92823 | 2026-06-18 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 858e46b6-d145-32a9-910a-fc79eff99ec6 | -15.43707 | -41.37548 | 2026-06-18 04:00:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22198c3e-30cb-3117-a23c-4b062b28db5c | -12.76619 | -44.55146 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1cc2d50-170c-329e-9c1a-7120295d6088 | -11.2494 | -46.63335 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 532f930b-7f48-36b2-af34-063488968c1e | -8.83237 | -44.79333 | 2026-06-18 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ba027c-8921-3d6f-9420-a8edcb3245c3 | -8.83307 | -44.78926 | 2026-06-18 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7490cbac-7fc0-38b5-be09-4ba8f1a5242b | -10.04207 | -48.11073 | 2026-06-18 04:00:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4195a1d0-cc14-3c30-b5e7-36665004f078 | -10.55177 | -46.23491 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dfd292a-5c4b-3b58-a3b8-483203216257 | -8.68496 | -48.31106 | 2026-06-18 04:00:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e94f8fb-f4a3-3fb5-b97d-9c92526ee76f | -8.97901 | -47.98024 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15148785-32c9-38f0-8c59-c8a2b6ab8064 | -10.91361 | -46.37654 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eff3a29e-4f0f-3868-9ce7-355442cb7e44 | -10.91241 | -46.43502 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aadfe28f-f7ff-3261-a827-7efe8f639174 | -10.04969 | -48.09858 | 2026-06-18 04:00:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc132af-1245-31b4-80d4-b5ab5166d791 | -11.25029 | -46.62836 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3d63c99-9bca-353b-8f2c-86afb521cea3 | -11.66115 | -39.01525 | 2026-06-18 04:00:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88ab6e7d-ad18-30b2-9ba2-388e762844c5 | -11.24852 | -46.63826 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68baf57b-3e84-3439-973f-293a40cdc191 | -8.97961 | -47.97701 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08bfaae9-3433-3529-a738-deacd2cb8191 | -11.48656 | -52.91978 | 2026-06-18 04:00:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99b40715-d8f6-35df-9877-5c62f030736d | -12.20248 | -52.7772 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 847aebb4-83e1-3158-9d43-7fa8953a69e6 | -10.65503 | -49.20485 | 2026-06-18 04:00:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04ffb200-e975-3153-86ec-fcd2e64981db | -12.23078 | -46.60654 | 2026-06-18 04:00:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2981b0c-1203-3751-9bde-98b47bd2ea0c | -12.2862 | -44.18511 | 2026-06-18 04:00:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97435da5-a7d7-32e2-90c8-bc53a575b4cf | -9.53737 | -40.33861 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| a8d45288-9fdc-37e3-956c-a6c9da772a74 | -12.07294 | -47.55279 | 2026-06-18 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8ef8741-1780-35f9-917a-facafcfa0bab | -8.90797 | -46.96554 | 2026-06-18 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 676ed363-fb8b-39f4-a2fb-95bccf339845 | -12.06956 | -47.55074 | 2026-06-18 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14bf28f4-f715-39e2-80c3-90c64849ab84 | -9.74602 | -47.87189 | 2026-06-18 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53b883df-7d20-30f2-85f6-bcfd247eedfc | -8.61066 | -45.98891 | 2026-06-18 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f945eae2-4a45-3d24-88c2-5fce984316e6 | -12.76707 | -44.54641 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 365f93e0-b2b4-3dde-9ec1-d5ebf3f407d6 | -11.94885 | -37.97813 | 2026-06-18 04:00:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 08f3123d-59a5-3aee-b0a3-80161d7a4b3e | -9.54014 | -40.34274 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| a4b567d8-104f-3906-a0ea-e2581f8f9459 | -9.74544 | -47.87498 | 2026-06-18 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc704884-009f-35ba-8c7a-f41f32e0c12f | -11.24841 | -46.63599 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ad9a613-5ea5-38c0-9292-e33c21de04c7 | -12.83818 | -44.36833 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ce3816e-0259-3c46-a36a-c6f6e83436d6 | -12.08848 | -44.97658 | 2026-06-18 04:00:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db0e384f-77c9-3f88-9b38-fb8c22ec55d1 | -12.07775 | -47.55372 | 2026-06-18 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5f0f406-05e2-35da-bd69-b902170637ce | -9.54072 | -40.33916 | 2026-06-18 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| d414c145-1dc0-33f0-a470-1913ff8ab21e | -12.74409 | -46.31697 | 2026-06-18 04:00:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb2be58f-5975-3f1a-98f6-03c9dd95dbdc | -11.97921 | -44.71888 | 2026-06-18 04:00:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94eb3db5-53fd-3a03-9113-ec8cc0ab29b7 | -8.93708 | -48.00399 | 2026-06-18 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22bd8d1-04a1-3268-892d-e8c0fc620dd0 | -14.20071 | -42.75492 | 2026-06-18 04:00:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4e9d695e-bf91-3dfb-b317-f297d695722e | -10.56244 | -46.22733 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dc364bf-bc05-319f-87aa-a012942b6266 | -10.56163 | -46.23196 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbe159cc-ab08-3cb4-9ade-f475ead4c86c | -10.81048 | -48.77329 | 2026-06-18 04:00:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
