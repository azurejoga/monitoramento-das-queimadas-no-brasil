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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0470b6da-b8ce-3fdb-92be-68f9422d887e | -6.12873 | -57.67415 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d80b691d-c45d-3cec-8e7f-7639ea2b500d | -5.87191 | -57.77823 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1682af3a-bd2b-3085-ab44-4ea45516ad33 | -5.9421 | -57.69095 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b44d25d-f1ca-3ac6-9bb0-e21e42632d60 | -6.19879 | -55.41807 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a886bea-d842-3044-ad8d-24def8237115 | -6.99999 | -55.87834 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f99eeb-0951-3bf3-8ab1-02dc833aedd0 | -4.09555 | -50.42805 | 2026-08-31 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65710235-077c-34cf-976c-d7da02acfc31 | -7.29941 | -60.57999 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 437558a0-56d0-33b3-9824-4a6d033be958 | -7.40025 | -55.15617 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88c4538a-a4cf-3331-bb01-7a375524e0c3 | -5.8941 | -57.75393 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 513c17cc-1ca3-356e-b73d-fa08ae12813f | -3.62815 | -60.56116 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 84f3ddf2-7ae4-371e-9a1a-bef21f6b9dfb | -5.9632 | -57.67672 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ad647cd-4130-3469-ba1f-db48de5f9625 | -6.1452 | -57.84916 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cce825ca-819c-3b9e-8e70-d6c7f5776fee | -4.96375 | -55.85248 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ccddce0-de40-322d-b481-b1c6e6e3a2d7 | -6.53644 | -55.11145 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aeb8df4-a7e0-3e48-bba9-fd9ef76ec1fd | -6.15717 | -55.96396 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbdfc5b9-c3b1-3ebc-9be9-eac77af64b3e | -6.89373 | -55.71111 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3072a09-653c-373b-b7c1-9cfce1251833 | -5.24928 | -55.91222 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ea6ff48a-217a-34ed-a115-ce424e40eb06 | 0.19606 | -60.50033 | 2026-08-31 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d891e3fb-3740-392f-a7d1-dde8117b10da | -8.38992 | -44.98901 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 872a0fac-c82d-3893-b121-f39702acc95b | -6.09084 | -57.72208 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 82e7fb5e-5393-3b41-a22d-71af06a739a2 | -5.87699 | -57.77013 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06d4ca62-a43e-348a-872b-adf6c6404c28 | -4.2881 | -59.95379 | 2026-08-31 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1058b42c-6409-35e4-a7f8-d530f1879102 | -6.93523 | -55.64465 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6f6dcb8-6f2d-3f85-aa60-5e7c5dd1e9c7 | -1.36411 | -49.26242 | 2026-08-31 04:57:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84f213cb-12d9-3c1a-beed-8dba6f22f9cf | -6.92336 | -55.71944 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| adaf61c7-be79-33ba-a595-a7105cff7616 | -6.93357 | -55.63346 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d9421972-0d41-38a5-839a-c7f8edc7c2d5 | -1.62418 | -55.17133 | 2026-08-31 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1dd507c-2f84-30cd-9f12-6d1c838310c7 | -6.37092 | -54.95334 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1ab705b-c1a0-37ce-9941-33a1760bb56e | -3.60886 | -59.07202 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40145ba0-d2f8-3ea4-8278-ce5c5ed507e3 | -7.97393 | -44.27914 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4454e7b2-0fc4-3bcf-b3a4-483372e6f65a | -3.82516 | -52.25052 | 2026-08-31 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06c0f16-2a6c-3293-8c34-764dee586f4d | -4.85468 | -55.83149 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f48fdd9-e90c-3242-870d-f7d5fa83755e | -8.08575 | -45.46406 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ada5bb7-3c79-34a8-bfc3-a1ca0032b139 | -3.61514 | -55.47781 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43ea45b2-8a9c-35ab-ae2c-c1da727d7c41 | -4.58784 | -55.9425 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9a1ddf7-9d44-3e32-8e84-d2d4033065db | -6.26658 | -55.41822 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae12bf16-458a-3938-99ae-8fbf66aa6df3 | -1.59945 | -54.40765 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c7f3384-16fb-36ed-b1ab-abfad1435e94 | -6.93346 | -55.69911 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df47c0e5-1dcf-34c4-876d-ab9875881d7b | -7.61976 | -55.2953 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c041b4d-aa89-33e1-ad99-0e233ac40414 | -7.01097 | -59.64735 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43b9ff4e-d762-3900-bb04-7c061fdadb13 | -5.24821 | -55.897 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d9778e4-0bef-3ab5-949f-41329e8cd2d4 | -3.41958 | -43.37528 | 2026-08-31 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5763d9e5-a184-31b4-a58f-a236198efa5a | -3.18968 | -60.15596 | 2026-08-31 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e437075-5470-3feb-9116-3ab0d6dd8d53 | -6.22495 | -55.49122 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a6c5d76-1e49-31e2-b0b2-20634d2b0586 | -6.88411 | -59.4034 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc26940f-765e-39b2-bd97-806f8e2b4ccf | -7.21119 | -42.74077 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa72b6b8-9b00-3d94-9718-ed2a91b73e07 | -1.59331 | -54.40307 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 37f498be-4822-3356-96f1-fc51c300599e | -7.98547 | -46.5209 | 2026-08-31 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 974103ff-9a0b-36ed-9afe-bbd533315f7b | -8.14802 | -45.47187 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f70f81ee-77b6-3b49-9f23-f619a5947d58 | -1.39414 | -55.74475 | 2026-08-31 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eeb8388-0c3e-3ab6-810c-3baf510d4859 | -7.10863 | -42.76299 | 2026-08-31 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93a442c9-7cf7-3458-b35f-aa368d21423c | -6.0762 | -55.54811 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f4b44e9-858f-3754-a64f-f01462a1d66a | -8.72697 | -45.38035 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c0a9f41-a9d4-3e47-9cfc-496897ccd256 | -6.81578 | -59.44242 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 628df2b3-cecf-376e-ba09-3584add017e2 | -4.08931 | -54.10373 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e5f92c5-0602-3472-b967-c5be0aaddecf | -4.85585 | -55.82411 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a65e661-3567-3975-85b5-f19ac76ebedc | -6.22875 | -55.61986 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49cdc339-7bb9-37f3-85aa-ff1e6368cda9 | -8.0796 | -45.46917 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fbcd7e82-6dbc-3a98-969a-0a0956562884 | -7.52522 | -55.3336 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3c5432d-21ce-3adf-b769-587ead051183 | -6.43437 | -55.77383 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e6f96e1-4dac-3a83-998a-f810d41c9d82 | -3.63044 | -60.54731 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81cb4170-22c4-393b-9dff-c90b985e6f6d | -5.48874 | -57.15454 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a353587c-3275-30bc-acf9-6ed446fe8665 | -7.97914 | -44.28257 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d252559c-fdf8-3d9a-8fc0-a9a3c2c15ae2 | -1.25716 | -54.55368 | 2026-08-31 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8a3fa1-7d28-3518-8b6b-45da2058fe49 | -3.58862 | -58.68817 | 2026-08-31 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed16d1aa-b599-3370-82bb-93087255a710 | -2.98098 | -60.93012 | 2026-08-31 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffc99a3-dbcf-3a23-ab5d-be3161e01a87 | -5.13114 | -50.63422 | 2026-08-31 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb2a3cad-6f35-376a-8e7e-1d7f2ddfdf65 | -2.93592 | -51.48332 | 2026-08-31 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e16f31-368b-313e-b7a1-c58d89a66bf1 | -7.98606 | -46.51659 | 2026-08-31 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8dd6042c-3f6b-36e6-be3b-5bb9f4305c87 | -5.88604 | -57.757 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a85ae87d-d5f7-3ef1-80a4-c3f26d388c43 | -7.9361 | -44.25079 | 2026-08-31 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f1fd1e44-dcb4-3977-9ae0-b671160bc574 | -5.87861 | -57.78363 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ab4e71a-b1ce-39f8-b2cf-29d8b59f598e | -4.14137 | -56.32614 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0d20e2-85a2-386d-b09f-45d4d578454b | -5.88647 | -57.75803 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e9fef0d-62a1-3227-b3b0-6adb6a86f34f | -7.97688 | -44.29944 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df72e73e-500d-3b22-8711-a728e77d00b2 | -5.24704 | -55.90435 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7c545087-1620-36c3-8224-d6cf3364ae14 | -5.49431 | -57.14278 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| efa1a0ac-4f07-3ca7-8fd8-676a2a058b63 | -4.39484 | -47.83542 | 2026-08-31 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e801a0a-de34-347d-bc0d-c148d50833ab | -3.45217 | -61.71613 | 2026-08-31 04:57:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecd207c9-780c-3eca-a53b-42ddcb45f9c9 | -3.58524 | -55.60122 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa10f728-a0e2-333c-a97d-20dc1d0f3c4a | -8.23951 | -54.94436 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141f0b9b-3b7e-3644-b702-e186c5e01b3d | -5.94646 | -57.68725 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 616aa6ea-09d9-3374-8863-4672d37ecad4 | -4.14076 | -56.33002 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1699c6f3-5afd-3c11-924d-0fc826c81b1f | -7.30729 | -60.5856 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d1421a27-2054-38da-a19c-1ef32f8de4f0 | -6.121 | -57.67429 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b327369c-66bc-33c1-98b2-65fca0b3e9ae | -6.60598 | -58.59553 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 480e6d73-d665-3fc5-b0cf-96c02bf64da6 | -6.80536 | -59.45518 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b763ef38-1b8a-3de1-b2fe-195f0ea429ce | 0.01002 | -60.6012 | 2026-08-31 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9654714c-ebe0-3096-b29d-7da11a375ed3 | -4.50141 | -55.46593 | 2026-08-31 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dbee3f0-0332-377a-bcf7-f9a8093a2306 | -7.62253 | -55.29932 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89664a8d-796d-36fa-848e-97781127e547 | -6.92558 | -55.72708 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0ff0615-534a-3496-93a4-315fe56b443d | -7.51358 | -55.27798 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6c9e18e-40cf-31e3-87cd-4942e04ae6e8 | -5.89518 | -57.75068 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c35ca58-07af-3ee4-aaab-0a107c010fa6 | -6.12508 | -57.67354 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 52c14235-62c0-304d-bafd-70a3afe16aa5 | -7.52688 | -55.34464 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e8fdcb3-7589-32ea-a6f7-f5b18c12794c | -4.28945 | -59.94552 | 2026-08-31 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b087cabe-e6d6-3859-bff7-4918ec40e356 | -2.89665 | -48.27293 | 2026-08-31 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e906bc3-65a8-3cec-a60a-0ef786aab484 | -6.68209 | -58.74746 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5884524b-de42-3d68-bfaa-5da9b086ba26 | -5.2562 | -55.89074 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 59371a7c-ff47-3c33-8102-7b54c0c1e00e | -4.35945 | -55.02697 | 2026-08-31 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README38.md)
