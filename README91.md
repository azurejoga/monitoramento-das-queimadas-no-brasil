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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceee527d-f646-344c-904f-d9104adf038c | -1.57933 | -53.75137 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f1e6e64-3318-34a1-b595-231674c5dd53 | -1.52966 | -52.66547 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e469292d-c5c9-3456-842c-0b3268680b14 | -3.78533 | -46.69809 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08d525d5-b3e8-3e85-b412-0c90651e3c38 | -3.10633 | -54.04175 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4980f2ce-99b6-3969-87fc-99abc65de087 | -4.18497 | -54.75868 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9770df88-2843-3825-b0d3-7c61ee7637f7 | -1.45241 | -54.53677 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009ba9cc-ed36-3939-a683-c1db5fcb4564 | -3.02867 | -51.53716 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 561f0936-176f-31d4-a772-0c80fc551280 | -2.96792 | -53.93728 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd1e7d0a-79ad-359c-b15f-05713ced4304 | -2.76551 | -55.33248 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3cacbbf-f840-3ebb-b76b-a7ec91fd701a | -3.83902 | -46.52669 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7af6bab4-e234-3f0e-9d66-9e2c0f90f9a3 | -1.90848 | -52.06325 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2cf8ec-c6b2-3ad1-af19-0d283dc6b74a | -2.86707 | -53.97579 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4e62e6-2e12-3ae9-8037-c05547483b5d | -3.02285 | -53.40885 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41cc72b-e245-31e0-9e67-6c965a952f93 | -3.21444 | -54.17312 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13abe1eb-7d54-372d-ba43-e502a786288d | -3.66782 | -49.89357 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58fcfa46-4bad-3d6c-ae01-d1a035a0878c | -1.14983 | -53.68509 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071d2201-6283-3dd6-9e3d-2617072b37ea | -3.03619 | -54.03759 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c4ccee6-2a9e-3578-aa54-dc774936b14a | -1.34036 | -54.98873 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4d2715c9-e8d9-3056-a0a5-4992bc6db4b9 | -2.97455 | -53.89501 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 809d9b58-4c15-3243-986e-f997c5a5cf5a | -3.39906 | -53.0288 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de061ffe-f561-30de-9122-fdb528354ce6 | -2.6775 | -46.60091 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae7d16ee-b2aa-3ad8-a036-7d7635743e28 | -5.22408 | -44.91419 | 2024-11-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d56fffb-4970-3bff-9745-067763846305 | -1.1436 | -51.67633 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed89b95e-70d7-33cb-a195-10a5c61ec48b | -1.08288 | -53.35769 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8868adf0-571a-306b-b84e-37913ce8d69a | -2.01342 | -51.19122 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6982fdb6-49ac-3ded-81d0-8112190adebb | -1.33422 | -51.43176 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb8cbae0-f3c2-39f2-8f4d-2848254e663f | -2.45963 | -53.96631 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdaf79ba-a5e0-31df-9d56-c61f470cfd45 | -3.25963 | -53.27735 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 364f70cd-0ff6-39ad-9393-ea04bafb7c6a | -4.09095 | -49.73997 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b898abbe-53bf-3a76-9912-ae0b7e8eaa15 | -3.0301 | -54.0546 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 168e7ed5-2719-3b1a-9249-78665bc7d4e5 | -3.10618 | -53.80996 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe820780-8422-3d4b-9ac2-49833cb5329f | -2.35887 | -55.87245 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc61356b-b9bc-38ea-9838-00084584434b | -2.42575 | -48.17125 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2af4e5c6-f44b-3e1b-99e1-25d857c4dff3 | -2.61199 | -54.00411 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c4178b1-1885-3528-9e5d-52850ab46b69 | -2.63266 | -51.76208 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81685a12-b639-323b-8645-e9ba1b213a2c | -3.11562 | -53.982 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a340e9b7-0085-3b1c-adc1-7f606f292e6a | -1.21495 | -46.76168 | 2024-11-30 05:01:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be08d689-19d4-3a2f-ac19-40b1bd00dd6c | -2.65282 | -54.09263 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6df08a-86d4-3704-bc9e-318392a30bdf | -2.9089 | -54.18284 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4be3b539-6740-383b-ab40-1a1acc72cecf | -3.96957 | -41.52402 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 66afe048-26ab-3307-b89d-19c3e270cf40 | -2.66484 | -48.7835 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03d40372-05ec-3270-8ddd-a010a663a55b | -2.28434 | -46.43783 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a505335f-38cd-37ef-beb6-8025846e5882 | -2.59049 | -54.07583 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 403fa630-fb2c-3901-80f6-17757f3995aa | -2.89943 | -54.1778 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f19845fb-edaf-34bf-92ea-cefd66b97521 | -1.16993 | -51.94405 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 677c5182-1120-359e-80d8-5bac9b3cb538 | -3.29794 | -53.83627 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66971947-62d4-3a8b-9887-fd0891209b98 | -1.37559 | -53.64837 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc621dc-2b0c-3842-bb45-46b7eb5f731d | -2.98661 | -53.28077 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 226d84c9-5307-3e3f-ac6a-5a871bc9bcff | -1.29832 | -51.72771 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09aca51c-2230-3450-83ce-642ccbafdc58 | -2.33325 | -50.67004 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03b63e5c-6b63-3c6e-a2e5-efea6aa2f88e | -2.34397 | -53.86246 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 809a78a3-c1d1-3f35-99ed-9632bb09ddfe | -2.22488 | -53.62332 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a2638e6-ca39-398c-ac45-f84f04f3b74c | -3.00048 | -50.50789 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af292291-4aec-3b11-8288-882cfc09d698 | -3.04567 | -54.04266 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2600ca9-0e4a-3303-a435-341f86759f15 | -2.72409 | -54.1115 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8888315-b5fc-396a-ba8a-ce2de54da2f3 | -3.2858 | -50.62795 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99e918e7-6cd1-3639-bc87-68e1bda4e08d | -2.76414 | -54.11771 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf610562-4b8c-3605-9e5a-c4dfe614509d | -3.24837 | -53.63911 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3014f8e5-74a2-378f-b108-2acd19cd98e8 | -2.04026 | -54.67072 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7089771e-f05b-3e5b-92d9-f03c25363b0a | -2.78507 | -53.20888 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd813a8a-8e16-323b-b268-a323c4291764 | -3.4907 | -54.03208 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ab7085-3bad-36b3-bbf1-a397ca3ff772 | -2.53881 | -54.00009 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb2b55ce-3a23-3507-aab3-e6bde4a5bb49 | -3.78109 | -46.69151 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0949c1ce-26ec-34d8-a1f2-0f4e96d6733a | -1.17221 | -53.41111 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a018e28c-2a54-399f-b94b-f33c0f55f626 | -1.5917 | -52.26854 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 586b59d2-578e-3bd3-ae92-0062811aa3c5 | 0.63248 | -50.56817 | 2024-11-30 05:01:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa81eaa-cbd5-3f12-ba7c-01b7c7eb6c56 | -1.25674 | -51.78292 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0faf326f-c849-3c12-ba3f-247c12482e44 | -3.42528 | -53.89193 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebb4369a-4e0c-348b-814c-bde9b2f8bb1a | -1.89484 | -54.54244 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 587efc04-32a0-33ec-b8c6-be953564143f | -3.49593 | -51.56972 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a0c974f-a2f9-302e-8913-f10caded2318 | -2.871 | -53.99437 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23403f05-5484-3881-8107-fe8eb161a38c | -2.89117 | -51.58352 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ba910c9-d969-34e5-9746-a7616b17192c | -1.80797 | -52.73721 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 022bb532-920f-379b-8995-95035e6a32f4 | -2.86123 | -53.32531 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eebd5bc-8451-390c-81c3-7b3fca753731 | -1.61983 | -53.8793 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e42b6d0-59bb-3595-b517-295600f2b929 | -2.86042 | -53.99632 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d646a5e-d07d-3872-b3ee-523bccc22c25 | -3.10086 | -54.04041 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c81eb617-3aa4-3a7e-8f2c-7483bcb19566 | -3.36112 | -49.75936 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9d08624-e827-35b9-af7f-c1d7ca9a1a80 | -2.86986 | -53.97982 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ab28448-2839-3ded-80d7-a19920ba66c9 | -1.10531 | -53.39018 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d09ea81-5f46-3ae0-87c0-1cf46f397c8c | -2.59622 | -46.57014 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f12c533-43af-3763-86c5-227db8bbaf77 | -2.52153 | -48.46054 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66ab6e85-af2a-32cb-9997-cb210c8c8fff | -1.56553 | -53.79571 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c6d49e-36fd-316e-9868-bb0c182a664c | -0.2561 | -51.60904 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf64b7be-023c-3e19-9a6b-2f6694ca9c3a | -3.74713 | -53.39511 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef46bd76-b694-3800-b10c-922aabc5eebd | -1.13216 | -53.21957 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449d24be-e676-344f-bf64-5dba1dc21307 | -4.19969 | -50.68423 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c2ff8f2-15dc-394e-8a42-4c9dfed15f12 | -1.09786 | -53.21798 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93a58d45-572d-3858-b095-ed4dfb894be8 | -0.95996 | -51.65411 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec21b7ea-1ea0-303b-ad7d-d5e516092048 | -3.35756 | -49.755 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03fe939e-2f58-3c48-8762-315c621dbc8e | -3.46686 | -53.87619 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23c6d304-deb9-3ad5-ba9d-513ea8c1d24e | -3.73021 | -54.22772 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea7027de-5f3d-3345-95e4-dab55b911efc | -3.25007 | -53.62832 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 34dc35e7-4099-3d81-898e-d5d59c06cd02 | -3.05627 | -53.17117 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 075cc39a-b2ed-3d32-b451-f1c7d592eef3 | -1.7012 | -55.02079 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8140e93-c0fe-3030-8e3a-c9ae333bb0d3 | -1.12005 | -48.32989 | 2024-11-30 05:01:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56cda8c3-2e9c-3f89-80fe-202c45f4427e | -3.49306 | -53.8185 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6b9ca59-7395-3eff-8890-ae74bbfa6837 | -3.39963 | -53.02506 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d47e1fb-6a47-3f9f-871e-3101d532cd16 | -1.13386 | -53.4272 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730c00c0-d639-3e6f-8ecc-b4a21aaaa31c | -3.60216 | -49.97664 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README92.md)
