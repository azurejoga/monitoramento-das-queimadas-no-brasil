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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddfa891b-99a2-393b-9c0a-0a426da9e873 | -3.10853 | -50.28679 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e2a2762-0e43-38a7-a0eb-04b63e3c062b | -8.11944 | -54.856 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 495b5b1e-f790-3ea5-8bbc-ae5351278583 | -6.13171 | -53.29585 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6f831e-15da-3faa-9fcc-f700eac4587b | -6.74837 | -55.08075 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1570d9f8-214e-3c59-b20b-46280243e561 | -5.17163 | -56.00797 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4cbab65-0378-3b28-bed0-1bd06dfebb2f | -3.25123 | -50.11936 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2320687-8f46-3d2d-a574-26a6c9b986d9 | -6.10674 | -53.09637 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44447de7-d921-3832-aef1-35cfefb18a81 | -3.10941 | -50.28062 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50998778-83e4-3839-ac56-94381f365327 | -3.10814 | -50.27527 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92219dd9-7cd0-349b-a825-b5b5b310749e | -5.85737 | -51.79498 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dd2dae15-8618-3386-9a7b-479d5d6cf3c2 | -6.07243 | -57.61325 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a656f0b-0afa-300b-a340-6ae4cd9f087d | -3.18466 | -51.24291 | 2026-09-30 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c1644881-59dc-37b1-a9bd-7579de5d440f | -4.02855 | -54.2057 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 232b1f28-b2bd-3193-8603-ac129009fb34 | -2.90825 | -54.09131 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 20fadc64-1b56-3d2d-af06-b2e3a09275eb | -6.75277 | -55.08761 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0e04f8-6598-34e3-b6c5-6094b9ce8367 | -7.55922 | -55.03501 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10f5a456-a661-3350-ba15-6805722c6e74 | -6.79363 | -55.82341 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdaca7d2-916f-38e5-be1c-9f2f8396dfd3 | -8.26916 | -54.75377 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efae86bb-9718-313b-9052-c002887eff93 | -3.15218 | -54.07812 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 11c72dec-b116-36ba-86ba-4e087aa44f19 | -5.87265 | -50.16727 | 2026-09-30 05:36:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3a70a879-34dc-3e64-bcb6-ddde62785197 | -8.31944 | -54.75362 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9cf55508-3fbc-3059-bbc0-10e86b909995 | -6.24143 | -57.75478 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44d9ce7e-0644-3bbb-93e4-8271bbdf91cb | -6.79403 | -55.82059 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a73bc4-3e5f-3a4f-9118-67a8e6bc9f92 | -5.8736 | -50.15989 | 2026-09-30 05:36:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6a7798f0-9f06-3345-a5d6-8659776938fe | -7.72871 | -54.79916 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b22fe59c-cb61-3908-b500-cec7cb09d02e | -4.02593 | -54.20061 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 232cf3db-4f03-3b94-be66-56fd31da1d10 | -3.63935 | -55.46456 | 2026-09-30 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f351d970-94d4-3e63-88b5-02b88617aae8 | -4.02495 | -54.20718 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 392769fc-2324-3bd9-89fc-962ede31c5e5 | -8.26869 | -54.75733 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ce37a28-2318-33b1-a0f3-662cf2725325 | -7.54765 | -55.04015 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dd1bf71-1b3f-3129-a33d-d62f6c859f9a | -7.17442 | -55.40825 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c018b5b-275a-3143-84af-903a15c82b5a | -6.13389 | -53.05726 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a6a4483-b88c-3718-81fd-a0809e4b8cc6 | -6.11072 | -55.69564 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4abfdaa6-3a53-37ef-a398-c0e66fae0977 | -6.34495 | -55.33038 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ffe6586-0779-3ebf-b99b-b5811f813feb | -6.14517 | -53.0635 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f591cbea-818b-3af2-b02e-e28233337893 | -3.38057 | -50.94175 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d7ba7eeb-7d81-3525-be98-3056f7db473e | -4.02644 | -54.19717 | 2026-09-30 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6f92ac2-4ce2-38c9-87b5-2bd173816dcf | -5.86895 | -50.16071 | 2026-09-30 05:36:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 313faaa8-7f3d-3cd0-b038-3cb517bf6f04 | -5.16658 | -56.01049 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1887a19f-b50d-3a35-8b7a-7a1e28d04d98 | -3.38474 | -50.95904 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0682877-13a8-3b4a-8916-a66efb71fdc8 | -3.00698 | -54.22266 | 2026-09-30 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22f26e59-cc92-3fdb-a26f-828e0e1d6eb8 | -7.5105 | -55.03419 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0797c0b3-e727-3bcc-8390-1e834c8918dc | -3.01115 | -51.0615 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 651447f5-ca58-35d2-9d24-0d8f9be093a8 | -6.11087 | -53.09365 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57561208-d6fb-3b7f-84b5-e737e3925760 | -6.49169 | -58.53522 | 2026-09-30 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4a3d57c-fa4b-3852-83d5-c6be4a6c18b0 | -6.11031 | -53.09792 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 208e7538-a266-35dd-8319-2b48dfb86b78 | -3.74695 | -59.41674 | 2026-09-30 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44008d10-4268-3482-8126-76f6a08eee97 | -3.18351 | -51.23954 | 2026-09-30 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4dbebe24-c9d6-3518-8fb7-b2fcccb3ed02 | -6.12854 | -53.05194 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6176a5ff-6bb4-3513-a922-a678558a232f | -7.55713 | -55.03889 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abeb32d6-549f-3e4b-8a12-e4fc9754ba4d | -7.72469 | -54.78777 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf3f45ed-895e-31dd-aae3-a49c634cb197 | -6.48757 | -58.53459 | 2026-09-30 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1cdad42-0f74-340a-8c2e-90a9d994fcb0 | -8.06349 | -55.34158 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ae1a6cb-5c7b-3dcc-9a84-6b8697e7cf81 | -3.19176 | -60.06389 | 2026-09-30 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dedce63-da3c-3c72-a315-04eb7c711d5b | -2.88472 | -54.87295 | 2026-09-30 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22d36017-5014-3d7d-94c0-8e88a5be3761 | -6.14576 | -53.05909 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32de9050-bbac-33c3-970f-4780546e360f | -6.20582 | -57.78806 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b118ba6-bca8-39ff-b05c-5a0d1a1f08e7 | -8.12148 | -54.85476 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 583a51df-6440-3fe5-84d6-93aa29e2448e | -8.31895 | -54.75723 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56229c15-84fe-3421-8621-264566c34218 | -7.54812 | -55.03679 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 742e965b-7699-3746-abf6-82aebb6f2bb2 | -2.90776 | -54.09461 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| d60dadcb-683b-3289-ad1f-c8050cfc9d94 | -6.13924 | -53.06255 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4dc745d-da39-3396-860c-7295de9d70e5 | -6.38153 | -55.13924 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88f98fa7-4f65-36f1-b1f6-7b03671a614d | -3.83451 | -52.26688 | 2026-09-30 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a285725-2f76-361b-bb32-a42c737bf2e8 | -4.84664 | -50.68549 | 2026-09-30 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b61dd90a-c136-364c-8f04-60b4c1c6d184 | -7.50958 | -55.04092 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fce05156-365a-319f-b798-31acf3462531 | -7.51097 | -55.03068 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b790602a-6584-3a1c-b4d4-f20de6cccaa3 | -8.31799 | -54.76443 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7108fe8a-0851-3514-afad-17ca3d32ff35 | -2.97903 | -51.05111 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ff0c1216-c7d7-3d4f-b0a5-f00984722595 | -7.50471 | -55.03686 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa90e10c-c083-3ae9-87fc-ccac71a74961 | -5.85591 | -51.79473 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4eb0de3c-7704-33f9-9d16-8ec05b437ffe | -3.01358 | -53.8804 | 2026-09-30 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90c4b7f8-cbb3-3ade-ae52-a60786bb3c57 | -7.43154 | -55.18094 | 2026-09-30 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aa09ab6-46cb-3ead-ac40-6354049aee92 | -3.10264 | -50.27961 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0aade3f8-9c86-351b-9315-899e5c5123a6 | -6.12818 | -53.27789 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f24a81be-9081-3ca2-ad52-b6f963bdf60e | -6.09615 | -57.63381 | 2026-09-30 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10681f64-916d-3404-96f8-f2f990231dab | -3.25168 | -50.1241 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482882e4-70ce-39cb-bbfe-4244c14cfef5 | -6.11529 | -55.69933 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00b1b826-b739-3fbf-b493-c057cedb015b | -3.38631 | -50.94821 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bcd2039-cd6b-3f24-8518-9d37d5a7dcec | -2.88429 | -54.87589 | 2026-09-30 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8916c3f-7926-3ce2-9beb-313587f08cdb | -6.10082 | -53.09548 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 276f4078-d43a-3a7b-84e3-49cf32739778 | -4.84393 | -50.6868 | 2026-09-30 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34f341f7-671c-37a7-b034-14833e1677fd | -5.1259 | -56.02023 | 2026-09-30 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a2b519-be0d-3c89-b459-a84770e2ccfa | -6.13114 | -53.3 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2fdd45d-2647-38c5-8f8b-d7ce2c110293 | -4.54365 | -50.77796 | 2026-09-30 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b82c0e5d-0159-3d30-a7cc-26d4b1d08816 | -6.1014 | -53.09129 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ebcae40-d620-3d23-8f1e-9e79a5769a59 | -5.87577 | -50.16352 | 2026-09-30 05:36:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92a9fdf1-64c2-32c4-8775-f6477aa69253 | -7.55136 | -55.04154 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57d045ee-0f35-3b1c-a7c7-14471eee0457 | -6.11266 | -53.09724 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6456d87-4c45-31fb-a6aa-0b0b6ed44691 | -6.12763 | -53.28193 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518e06dc-1d12-366b-81cb-e8ad7f5a1899 | -6.10991 | -55.70142 | 2026-09-30 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c3a6ea-5379-3d22-bd9d-939b63a9c157 | -6.10495 | -53.09277 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19dc1177-e59f-33f9-a341-290394422995 | -7.55757 | -55.03559 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0736bdf9-3d09-3e0e-81e8-0a9b121ce2ec | -3.17826 | -51.24197 | 2026-09-30 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151eb9bc-1a88-30ad-ba25-a87cd42eddef | -6.12708 | -53.28599 | 2026-09-30 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eede18e6-5c44-3fc6-ae7c-746d052866e1 | -7.50383 | -55.04337 | 2026-09-30 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9794565-0ea8-34e0-9437-be11800bbd4b | -3.37245 | -50.95178 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d93b55a1-ec3d-3214-91d5-f689e380dc2d | -3.25236 | -50.81435 | 2026-09-30 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71a140f9-874e-3e20-9b4e-18ef9206533b | -3.8315 | -55.79522 | 2026-09-30 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 805721b5-06a2-30c5-9546-9087f2abec8a | -3.37901 | -50.95256 | 2026-09-30 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README60.md)
