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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61df1c6f-ea3b-3c6c-8d9f-aa89e18cb922 | -2.80379 | -54.10789 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08f3175a-3fbd-3610-8598-c61a8e835bd8 | -2.93104 | -54.15901 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e31e3a4a-d57c-3a54-8663-3a915b79c92d | -2.22059 | -53.70346 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b3ede93e-1c11-3f72-b856-c13c3db160fe | -3.11561 | -53.72766 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 7a6c3373-f54f-3372-b591-3645a18e3b4c | -3.00795 | -53.87011 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0743eb0-3bda-3e4c-a8d5-7b27f865a6c2 | -1.86715 | -50.62777 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7e5698-254b-3b1f-959f-9029674983fe | -3.28225 | -53.82314 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0733fa64-4540-3a2b-a116-4d2fc082fa52 | -3.17941 | -54.07842 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6df1d12-7430-3325-a57c-663b445da845 | -3.05957 | -54.17114 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06684d73-f2ad-38d0-bc71-40db1c0b3bdc | -5.12449 | -42.40397 | 2026-10-04 04:55:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0bacfacb-ba12-347a-8c41-4df28bcc392f | -2.91789 | -54.09568 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d724459f-34f3-3792-9bd8-671d3077692c | -2.2417 | -51.91466 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3236239e-2d99-3088-8966-60f9cfa15666 | -4.28315 | -49.72925 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cd52d94-cd1b-3b5e-8f27-6736144d6a77 | -1.74479 | -55.23778 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b3d3664-799f-3a0e-9cb7-106b22effe94 | -2.97121 | -54.09721 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f23263ae-f684-3fed-a024-9cfb44ab9fb9 | -3.94243 | -49.52506 | 2026-10-04 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a4241c8-14d5-3a19-9e23-4179c834ba32 | -3.17655 | -54.09636 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f116b87a-ad6b-35da-bc64-93c8f1fc140f | -3.70573 | -50.66193 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 83e8b8d7-5d17-3e53-99b2-b2f4993f0c26 | 2.00785 | -61.0923 | 2026-10-04 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56b49472-b8e6-3fc7-bb30-226c2231ac19 | -4.28394 | -50.27783 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9f9b490e-41aa-304b-9f02-d2ef2614fc6f | -2.59156 | -51.84818 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 496486b0-503a-349e-9bfc-b8b41450a65e | -1.99471 | -54.10646 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7013121-b38e-36d5-b56b-57992c8ae45f | -3.89817 | -49.69764 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf41b729-f918-3374-bfa2-da7f56b265a9 | -3.81737 | -51.54382 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f20fac2-739b-30ae-859a-fc32d19745f4 | -3.13344 | -53.74744 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adaf563f-89cf-3dd8-b73b-b9f1b0c93bfc | -2.24514 | -51.9152 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e163f14-229f-3537-8cf2-3304efbf9bae | -3.27305 | -50.01937 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef4fccc5-ad46-3964-bce5-b14fbc7505d8 | 2.5162 | -60.99557 | 2026-10-04 04:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbd1e5ef-4d58-3d96-aaac-4785972be5b9 | -2.95574 | -54.10181 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a0dbde2-e819-37ce-8b49-7d2c547ba7f0 | -2.81064 | -54.11371 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bca850ef-4c54-34c3-b32e-2d6f3c92d480 | -3.10983 | -53.74011 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 09abeb83-4120-3017-a3a4-ef44bc36fe3d | 2.3428 | -50.75534 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e638ee0-da15-3ee4-9479-c2ccc4a44361 | -4.29127 | -48.56351 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b14c9f-606f-370f-bd59-3f2270ce2817 | -2.92094 | -54.10086 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cac93e7c-9b17-3251-956a-01ae821592e9 | 0.60265 | -51.56143 | 2026-10-04 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45c8b229-7aea-33d8-8d1d-0a216c03aeda | -2.96316 | -51.51231 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ad48996-0efe-3a2f-b3c6-09d89a03ea32 | -3.46893 | -50.10671 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3152fb4f-085a-3e96-b384-0068f3c09d2b | -3.08562 | -49.53455 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebcab2d1-e23b-32b6-bc4d-ddc7dfd36c8e | -3.51685 | -54.62177 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3206193a-f985-30fa-98da-ef0b542b75e0 | -2.84807 | -51.28966 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fd1e431-5b38-3e7b-972e-a043c9d5de5c | -2.80602 | -54.09413 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 955045fd-fa8c-31a2-9d46-4b46024f8624 | -3.2798 | -50.40297 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 162c2469-6d0b-3680-97d5-a851e48d88b4 | -2.88771 | -54.13784 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32c50fa6-2d3f-356a-963b-d89e3fd3430a | -1.1052 | -54.14511 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 833abe44-03b2-377c-900f-85fcef01e9dd | -4.46437 | -50.97343 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 553927f0-5e73-3d7d-82c8-6054bdceba3e | -3.07729 | -49.54396 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5d0a149f-9a57-3eab-bbd0-31fe3e296e6e | -4.14891 | -49.69703 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1879eb8-af6f-3294-8b87-c00781d6673c | 1.92956 | -55.72364 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f96de7ad-9b9a-367f-913a-d650605329bd | -3.06153 | -54.16347 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93b3732b-b739-3f7b-b622-a87e92de57b9 | -2.58117 | -51.86911 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d671661-4744-38f5-8d89-5b1859bbe413 | -2.95606 | -54.11833 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 394f7ec8-b546-3d3c-b7c4-cca5ee2387eb | 2.35587 | -50.75379 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac8cda7d-6c1c-3255-987d-dd02fdbae98f | -2.83544 | -50.4746 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3411a6e6-90ea-3ab4-9fd0-9df4d74583af | -4.26135 | -50.74244 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6080f37-7fa1-397c-8cc2-95a15dd53cbd | -2.69235 | -49.03491 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 446c9b5b-9d4e-3729-8d6e-56c320692aa5 | -1.09579 | -54.10378 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03e7c2ed-80be-398f-a9ad-b3cbb0364f45 | -2.97877 | -54.09843 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e13c1ccb-0723-3da1-a7a4-5a50819d0776 | -2.82961 | -54.11678 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4cb0a0ed-3d81-3bea-ae23-4b01888e14f8 | -3.04891 | -54.21193 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 014f7859-6f47-31d6-a173-69e9ed1b25ad | -1.70076 | -50.0331 | 2026-10-04 04:55:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3274d03-0294-3944-a753-cbd82ef8cd06 | -2.88228 | -54.07589 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79671f5a-4bb7-3a21-8b2a-f2df1e540c6a | -3.12301 | -53.72885 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c24b5c99-2288-3140-b7b7-22140735abea | -2.92577 | -54.16759 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81a6b7b8-4f5a-3d5f-b67f-423d8dd8dfec | 1.91646 | -55.76548 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48d52f79-11f5-3e36-8f6b-61a31ce6fa8b | -3.04207 | -54.21229 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc7961c6-13c7-3237-aade-957c0e51559c | -1.68683 | -48.1999 | 2026-10-04 04:55:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c730f6ab-43bd-3d65-88bb-72975847644c | -3.29429 | -53.84293 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d4e536-c41c-3199-8c21-c974f4a670dc | -3.12625 | -53.75617 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ba6cdb1-f1f2-33a9-8c51-e73d742f3edb | -2.9716 | -54.09968 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a8e8668-9406-3742-aa9d-32a0adaad060 | -3.11584 | -53.75002 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 788aa8f9-f0b8-3dd9-8c4a-ee99bc877a11 | -3.52175 | -54.61943 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6f197c9-64a4-354e-89aa-6e821fd31698 | 1.76263 | -50.9305 | 2026-10-04 04:55:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15bd0c07-90b6-384c-abf8-9603a416409a | -3.76096 | -49.56464 | 2026-10-04 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| d9e06ab4-c938-3b08-bf1d-cfc7cd8bafaa | -2.92774 | -53.93946 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5684fdc9-af65-3b61-9e35-628cee00caa8 | -2.92492 | -54.14858 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f8648fc-65fa-342e-bb6e-0a61ef97c6ac | -2.81434 | -54.09075 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 522cb10a-4405-3cd8-acf0-1dd518002def | -2.96668 | -54.10116 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a75b1b83-53d7-33f3-8548-5dbf81ffa1d3 | -3.71016 | -50.65553 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aaaf381-6164-32d9-b588-18c6ad1ed4bb | -2.81675 | -54.12414 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bd0aeaa3-f988-3d9c-a6da-17e5ebb0f2a2 | -2.57715 | -51.87225 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 665b0f6f-18ed-3460-a7f1-a23c014d66bb | -3.13928 | -53.735 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1273d985-d1e5-38f6-a137-0c8b08dd09bc | -3.28386 | -53.83677 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccb37fc1-56c8-3569-9abd-f0f1f2a2eb32 | -2.92362 | -50.42807 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9db5ff-4150-3f63-ae9b-d0593200f2f5 | -3.18479 | -54.09318 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7dc6c92-a721-3d69-b102-688769039eea | -4.28171 | -50.27038 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 1de161ea-f760-306d-aa58-0697cbde9699 | -5.03979 | -44.46443 | 2026-10-04 04:55:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20bad2a0-ab5b-3beb-984e-617a9ba65996 | -2.96503 | -50.31768 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6102330-9881-3aaa-9fbc-2700ef353a5b | -3.51141 | -54.60611 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d464ad9a-2b99-3036-b092-fbf197e4f749 | -1.09813 | -54.11419 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c980cbd6-bb5c-3eed-87cb-890a6ad56879 | -2.25336 | -51.88611 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51d7cbe4-5ed8-3137-8fbf-9be3844834fc | -2.98923 | -54.03485 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a97300cf-e1de-3069-94d8-c1ce4b22a192 | -2.52025 | -47.52811 | 2026-10-04 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3bde736-ac34-35ca-8056-c7d3732219dc | -3.70193 | -50.97796 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74760593-9d16-3863-b15e-4f5d27a907d4 | -2.80528 | -54.09871 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f23c476b-a684-3806-8a3b-72d56e1fa7c3 | -3.1244 | -53.72015 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e04979f7-a046-35ea-997a-1ebad468e37b | -2.9141 | -54.09509 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06c98867-7fc7-3b26-b3b7-d58916bcdcd4 | -3.58405 | -55.31541 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7143d541-cc80-33e6-8062-84201129c146 | -4.26407 | -50.74286 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a1ef3d6-686c-366f-9576-92ee8624cb48 | -3.50678 | -54.61023 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e6122d5-4794-35a2-9e14-9f63aa480ae7 | -2.81221 | -54.12813 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README39.md)
