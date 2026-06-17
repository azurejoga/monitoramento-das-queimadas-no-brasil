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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d6ef95f-11e6-31d7-993e-486105163abe | -12.21207 | -52.7932 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9238756b-9417-36b1-9c2c-296e95f05558 | -10.90268 | -54.13226 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e17b4594-5a40-3d46-aa2d-812e5543a8e5 | -10.99146 | -46.47393 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38205d66-d0ee-3b91-b327-69a81c084e49 | -12.76893 | -59.00602 | 2026-06-17 05:06:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e1b77e0-39ce-3df6-8b7a-098f22877a93 | -12.22925 | -52.78117 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e7ec08c-24ad-3ec1-8893-8a0ca59135ea | -10.79587 | -65.34659 | 2026-06-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac93b1ab-7d33-3eda-9ee5-30ed49ea89c0 | -12.21338 | -52.78367 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 314.2 |
| 59ef0f15-f6c2-3d32-83f6-dcb0c9e9e1f0 | -10.54353 | -53.72237 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e4802d6-119e-37b9-94d2-557d0cf1ff0b | -12.19588 | -52.7744 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 42e5454e-119f-396d-9aa1-9d440df54a9c | -11.53824 | -52.77482 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4667a49-553e-3e8c-8876-fd704e935816 | -12.4341 | -58.40073 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62cacdc5-5322-375c-8a88-5dd19b69d29f | -10.36087 | -54.09943 | 2026-06-17 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99fed7ce-24dd-3e09-9e47-e82790b9dc55 | -9.18998 | -58.0551 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0812e17e-5fec-32ba-82c2-43738ee5f416 | -12.199 | -52.77976 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a30b98ad-3b18-3cd5-b24d-3ffc3999c849 | -10.15422 | -56.61285 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 058e7ee0-a749-3816-ac73-ba1a0445f0a0 | -12.2028 | -52.78033 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1cd439e5-f5ca-3ce3-9f9c-e0674996923e | -12.43352 | -58.40437 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f482a4bd-1d0e-3187-9af5-06a868ecf277 | -14.09467 | -59.45636 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abf125fb-47c5-327b-a7be-f4b6591e79ce | -12.20592 | -52.78568 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| f882d22d-49e9-3354-8cac-ae530b9c923a | -11.59155 | -55.33698 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4211e467-afd1-3296-8617-c093ab6deb5a | -12.20212 | -52.78511 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2066d3fb-1d2f-345a-9b69-786e6aa315bf | -9.44208 | -59.20897 | 2026-06-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e46a6365-39d3-3892-a36c-32a5cc09a753 | -12.20524 | -52.79044 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 0532c59d-d4a4-3301-8f7e-2122813d4ad4 | -10.54413 | -53.71832 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc1647c8-c413-3dbe-b925-70d5b44f83c4 | -10.12697 | -52.17815 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a42383a0-aa3c-3009-8807-d71179c7205f | -13.94151 | -53.56677 | 2026-06-17 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 620e49f9-3979-3248-893f-2c02f35e88e3 | -12.17618 | -52.77636 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5fe3126e-ff87-3b08-a2f5-bfcde195c152 | -12.67916 | -54.57699 | 2026-06-17 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 940f6768-f147-3078-bb80-002fc7fd8e0d | -10.55921 | -46.22261 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f0c174f2-0d01-3f86-ae78-5733b0d99915 | -12.17931 | -52.7817 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df53e89d-3a2c-340b-a49c-e206fb91ad59 | -9.88424 | -52.43905 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ba5d2f9-6e30-3047-bb04-4c49b7b33063 | -10.12313 | -52.17762 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7dbf13a2-bef9-3371-83e2-772010afb880 | -9.72836 | -57.67216 | 2026-06-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dca08b0-f926-3ed1-b388-f112e0c8cc5e | -12.47248 | -55.12159 | 2026-06-17 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e067363e-519c-36e9-a7ac-085b6168eaa3 | -12.22164 | -52.78004 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 57c7b538-50a6-3fe9-b51a-5e1812350c21 | -11.54134 | -52.78006 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e2ebb31-1f66-3cec-ae1f-cfd0918fecc5 | -11.35413 | -55.82403 | 2026-06-17 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4539a3d2-6454-3681-bb88-881355309b30 | -12.10862 | -51.99031 | 2026-06-17 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb176b8-085f-3e43-8bed-29d9f6e235a3 | -14.10025 | -59.46521 | 2026-06-17 05:06:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4f78535-0dd5-33b7-92eb-b3c80f5038b6 | -11.67174 | -56.76446 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a56dfbe-f4c6-3632-907f-2ace6a12ecd1 | -11.48233 | -57.10696 | 2026-06-17 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47a694ca-205f-3b50-970c-0bb240ca46bc | -9.20517 | -58.0689 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6af75b3f-3263-3bce-8825-3b30334ca817 | -9.20856 | -58.06945 | 2026-06-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b51c529-00e7-3110-800b-0fdfa0efb1a6 | -12.84231 | -44.36918 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| da05b21c-f797-31fe-977d-d2c553119c90 | -12.84167 | -44.37495 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 3a89adc0-30be-3ef8-b165-e458a30297a2 | -10.78398 | -54.10349 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4de77974-a5bb-341a-88b7-13549840e347 | -12.2286 | -52.78594 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6316bbb-7e88-3024-a99b-815548bcc856 | -10.15807 | -56.60989 | 2026-06-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc0d718b-23b2-3585-abf2-cddcb50602b9 | -12.19003 | -52.78817 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5cac5a52-1cc0-3ceb-b296-2701f0e57ebf | -11.26529 | -53.95552 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58eb29e2-a22a-3ee2-93a1-e490d6d0b463 | -12.21588 | -52.79377 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bd8a3863-89e9-305b-b4aa-3b95beaaccce | -9.88347 | -52.44084 | 2026-06-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7271227-0d29-3d27-a27d-19ee0610a064 | -12.22794 | -52.7907 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 583bcedc-2867-3590-8f20-a1db9af9290a | -10.56446 | -46.22742 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 281d46d1-ff2c-3118-a68b-086aa18d9e9f | -10.60298 | -44.32249 | 2026-06-17 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ae1113b-bb72-3926-9b01-10eeaecb3c3b | -12.21523 | -52.79852 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e0b49f31-cda0-3207-9268-8ca49c9812d4 | -12.23484 | -57.27596 | 2026-06-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a9aedfb-33d6-3ff5-b13c-ca3a065c36b4 | -12.19452 | -52.78397 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 56999a8b-b7ae-3915-84d6-0c77d0ee8d97 | -12.429 | -58.4111 | 2026-06-17 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e861534-c4bc-3e1b-b14b-f5f84feb1837 | -10.77291 | -54.10585 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703d3e51-4b45-3670-8c7b-481023061250 | -10.76826 | -54.11318 | 2026-06-17 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6045590-ae30-36f2-999f-dc0d70e1fc71 | -11.18147 | -46.59352 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d744b9-7d22-388e-b5de-181421cef9d0 | -11.53757 | -52.77947 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6a257d0-75d0-352c-94c7-c7465e5cacc7 | -11.23525 | -46.60274 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ae3496e-1bf6-3176-b58d-acf15d8d58a7 | -11.91485 | -55.91492 | 2026-06-17 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad5571b9-4edc-3a1d-9b04-c9fc7ddebc28 | -12.07902 | -54.60554 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f6a73e7-0b95-365a-b2b2-b20da7b031cc | -12.54681 | -57.19735 | 2026-06-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a85cdc-4ffa-399d-9839-ea3d3392db7f | -12.23306 | -52.78174 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69b78311-a507-3599-b126-e8dd35db83c0 | -9.44275 | -59.20492 | 2026-06-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 006aa0f5-8ed8-3bf9-9a26-bd0e51438d39 | -12.84639 | -44.37192 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 91321068-bc03-323f-bf05-f4d8f6aefd56 | -12.18827 | -52.77327 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c4adead-7ac6-3261-a07b-3dce69462e15 | -11.54268 | -52.77073 | 2026-06-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a7432dd8-2aea-306d-8073-75ade29b9a3d | -12.17305 | -52.77099 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 46bd5608-b816-3b25-81fc-314a43d7af38 | -12.18691 | -52.78284 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2fe71cee-db41-336d-a1f9-799c40bdbef0 | -10.98547 | -46.47568 | 2026-06-17 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2a80347-58ba-3fb0-8990-7beb9763ac22 | -12.07845 | -54.60944 | 2026-06-17 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dc1e4e97-0c13-37f0-b10b-46ffeb7afeec | -12.84829 | -44.37586 | 2026-06-17 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| b3cbbc7f-026b-350f-b076-e008e86f5b88 | -11.72128 | -54.49469 | 2026-06-17 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a81f618-4c6d-3889-a6ea-0933594efb08 | -12.22545 | -52.78061 | 2026-06-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6d9b0016-5ba9-368a-9601-c2fa7c94c9b0 | -16.25428 | -53.68285 | 2026-06-17 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e5c5fd3-af3c-3742-96e6-893526cb78da | -16.1133 | -56.75362 | 2026-06-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac17d493-b0f8-32a2-8151-a144d0e45bd6 | -19.1727 | -55.18024 | 2026-06-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ab7491e1-56d1-3fa5-8d3a-f4d1df09a467 | -15.071 | -55.81739 | 2026-06-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed6ccef4-7073-3f67-b4eb-4023a7546a4a | -16.44852 | -46.35894 | 2026-06-17 05:08:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2062631d-e6c8-3c34-8639-5a7245ff2797 | -18.46075 | -54.70629 | 2026-06-17 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca9008d6-d8c0-3792-addb-eb0c98d0e939 | -15.42265 | -56.30664 | 2026-06-17 05:08:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1ddc896-4f0f-3d12-a25d-f213acd1b507 | -18.41587 | -54.54582 | 2026-06-17 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68162720-6948-3968-96b8-4f91475285bd | -16.4545 | -53.65725 | 2026-06-17 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aae7b4c7-27b6-3465-ba12-2df71b264898 | -15.07157 | -55.81354 | 2026-06-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a611de1c-e0fd-3b3b-b88e-587b42e632df | -12.8548 | -44.3625 | 2026-06-17 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d8535efb-3a83-383b-aca8-e04189f6f332 | -12.8354 | -44.3657 | 2026-06-17 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| c03a0438-4e3d-3644-878f-29eb515b5ac0 | -9.3423 | -45.4765 | 2026-06-17 05:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 6c554aa2-bd7e-35a5-b1f5-6b658a5a12de | -12.8548 | -44.3625 | 2026-06-17 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1cc015e3-cb97-32ea-9d99-869b392ffd1c | -12.8354 | -44.3657 | 2026-06-17 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| be8b9012-9a5b-379f-a9b1-902c8a47dd87 | -9.3234 | -45.4787 | 2026-06-17 05:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 9e2c86ba-85cc-3d8b-a25c-82df2c2c92d2 | -9.3423 | -45.4765 | 2026-06-17 05:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ae32e613-d129-313f-9316-94976f38ba18 | -12.8548 | -44.3625 | 2026-06-17 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 08a53cc5-a2da-3270-9fb8-7f900699b990 | -9.3423 | -45.4765 | 2026-06-17 05:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e6832130-afc3-3a9c-887e-41fc702250b4 | -12.8354 | -44.3657 | 2026-06-17 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7fbc5e96-3df5-3260-9190-b062844515c4 | -2.73749 | -58.1903 | 2026-06-17 05:38:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
