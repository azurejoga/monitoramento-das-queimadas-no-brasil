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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4656a568-e230-3a7a-98bb-a3718d10a388 | -3.13328 | -53.71474 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f40afa60-1eae-394a-aeca-adc216694817 | -4.05597 | -59.36296 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b3345e83-708d-3827-9e77-08cd161c0522 | -7.65062 | -44.3795 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4802f9d7-2cc7-3594-86c5-e1838fd37909 | -6.46516 | -43.59619 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 383f0c19-98a6-3ea3-af9a-31a2c5d29372 | -3.50516 | -54.61846 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c02f4a27-711e-3e3e-b53c-533ae518cced | -3.90324 | -41.5752 | 2026-10-05 17:15:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30f1e69c-860d-3b9d-9e35-892e9f0e205f | -2.85921 | -51.2811 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9622bea3-e59e-3cb8-bbdd-f97b762a8903 | -4.46304 | -54.95673 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92397230-488b-313a-9127-b43d8dd98b3f | -4.84941 | -42.20279 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a36859cd-ff33-301e-8bee-e6473a6189e4 | -8.92267 | -66.84694 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 142ad973-a7ee-3dc8-92f7-6b607c30df39 | -3.08041 | -54.1622 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e334fb63-3de5-312a-9a59-c5bea76e177b | -5.113 | -42.63688 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 077d6eaf-7a46-3c37-8d0e-adcd1739fcf8 | -3.07973 | -54.17996 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a5366bc9-a702-32b9-8573-82d1e5ca15e2 | -9.12576 | -64.38528 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1be506fc-73f3-3185-88ea-65cf3fe53e7f | -3.47627 | -55.43119 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 75f65e1e-64fa-325b-95e3-695223fc2816 | -6.00027 | -43.78745 | 2026-10-05 17:15:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf2a0c6d-eb15-316a-bcc2-152b0fb209c3 | -3.20803 | -42.44392 | 2026-10-05 17:15:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4b0e610c-4e70-35c5-8de4-137a14e9eaa5 | -5.4464 | -42.64199 | 2026-10-05 17:15:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e31662c5-9a70-3961-a212-ae86fb258954 | -3.79191 | -42.9471 | 2026-10-05 17:15:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a6a4d37-82d4-3058-816e-588a2374b0e4 | -8.0423 | -46.83256 | 2026-10-05 17:15:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58336495-3afd-3910-a5cd-b3e0bef6f9f2 | -4.43516 | -43.4248 | 2026-10-05 17:15:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5c66214f-cb76-3a2d-af45-4cf9861b7108 | -3.31461 | -53.85701 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c9ccc697-af65-34d5-a675-868294d5a6ce | -3.28192 | -42.25745 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6005c68a-605c-3a46-a902-b02fbfc9778c | -3.10116 | -53.70538 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 542ab3f4-8f48-3d5a-8a86-f052421c9467 | -8.53046 | -54.58343 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3d715992-ad2a-384c-82d1-2a632a40bd8e | -4.27082 | -54.67224 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87cdb0f2-1e53-363f-b7b9-54ccab41a8db | -3.11116 | -53.70387 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| da92ffba-c431-3c86-a9ac-b0861b641fef | -2.85097 | -51.29938 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e5c5daa-6ead-368d-8862-06bf40eace3f | -9.11648 | -64.36209 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0390e66-055e-312a-b187-d007b50f707c | -8.65973 | -54.54121 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f361348e-788e-3f65-aa52-d71940b64811 | -2.70103 | -49.03826 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0d654c4b-99e7-3a4f-a8b4-ae3fd59519c4 | -2.99493 | -54.11228 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c64889e3-763c-303b-9c9c-f2d1f5147f51 | -8.59939 | -67.13953 | 2026-10-05 17:15:00 | NPP-375 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 61b0da39-a21e-342c-beac-542b88666d18 | -10.30206 | -63.39874 | 2026-10-05 17:15:00 | NPP-375 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cf81db3a-a005-3ef8-8231-33ba487f211d | -4.24874 | -50.75238 | 2026-10-05 17:15:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3fb26a53-c936-3aa6-91bf-5a77e91192af | -8.47201 | -49.45074 | 2026-10-05 17:15:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3eadde26-c48c-3f15-897c-e77a75dc8f7a | -3.27209 | -50.40247 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| dade8c4b-b600-3c90-89cf-3a34b55823e6 | -4.05619 | -54.04329 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b082a7cd-5184-318a-9b52-d557defcb887 | -3.22926 | -53.87705 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 751c46c5-bb10-322f-ad53-a8e438bd660a | -6.3482 | -42.54613 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1d583745-9285-3ac4-bc05-265691559a7f | -3.97427 | -59.34153 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f84e2bad-cdc6-3356-8b38-fa14ed486111 | -3.05499 | -54.21617 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 6cdfbcfe-e451-3d1a-b60f-38bbc9d05cb7 | -3.61581 | -55.50397 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f1a292b-1ae7-3903-8e25-f54e9ee5abf0 | -7.90262 | -44.18896 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb819b32-8964-3213-b29a-196dd8d3ca8e | -4.44739 | -54.96625 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 760d94b0-9bea-3c60-ad10-20c2fe1ebf1f | -7.82956 | -45.29951 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0353af2d-67d6-3a63-9245-2398a1e7524f | -6.67691 | -55.10476 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88255334-ffad-3474-a6cc-20bf02927515 | -6.71347 | -45.22338 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 858083e6-3d4f-3f0d-ad7e-dacd81c49583 | -6.20299 | -44.79993 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7e4c20c0-8b1b-3497-81ce-0ee21f53969e | -3.04782 | -54.21373 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed8c1ebb-50e1-33f5-bbfb-22a93f1f3fc6 | -3.82058 | -41.80429 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 260dc0ef-f080-3750-a3d3-1059dd8f478b | -3.60421 | -54.05097 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4250833e-e473-3333-9501-14e8abecba07 | -6.91246 | -43.66719 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ab5c2a26-7574-3c88-a75a-c09ec6bd1c8e | -4.85056 | -42.19782 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 2d9c4291-e3a1-3ae4-af83-0665b81a4d3c | -7.21856 | -55.18716 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22e3a018-2fb0-3786-ba12-17007c7ffc22 | -3.67198 | -54.53857 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 4fbea26d-640c-327c-bbc9-171a3a497389 | -3.08426 | -54.16515 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e2967550-4886-301d-9c5a-082b49376c00 | -5.83131 | -45.01131 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 394760bf-87b8-390d-b49c-f7c6197a0ee9 | -7.11328 | -55.72181 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 364e7220-d5e8-31aa-8634-d61c4e91adbb | -9.10371 | -64.37497 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85f72bb9-6125-3201-9aa1-142950a49c38 | -3.47447 | -43.25373 | 2026-10-05 17:15:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f77fd07c-84ce-3e22-b961-42579f5fe009 | -8.73398 | -47.06963 | 2026-10-05 17:15:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3205450-d54e-39e8-bf8e-2c1c7c7da3c2 | -3.10266 | -53.73719 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 56bd351e-eb22-3de3-8a25-a3dce684f479 | -6.07629 | -47.66357 | 2026-10-05 17:15:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ffcdc549-a87e-3ef9-aa4d-643e6341fcd3 | -3.8144 | -41.79715 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 449ceb35-6789-3587-80d5-28898c28531b | -4.26566 | -59.20959 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 162ac701-08d2-34cc-9872-ee16fcb669f3 | -6.72719 | -44.28435 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 98c1efd9-38e4-3f1a-a40c-6c4c25ba1959 | -8.5303 | -54.60577 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6bcf679a-479c-37a1-b7b5-6f42e53e39f5 | -2.96013 | -54.10696 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7f7f0acf-cdb0-3d14-96be-37d88565095d | -3.54879 | -59.48988 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4252fafe-e1af-3596-b393-cd2752620414 | -0.38164 | -52.08159 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c3f789a1-79b6-39af-82b6-509a58294bfd | -2.98006 | -54.10393 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7597ecc-bd14-3877-bc63-4b9e7db81257 | -0.73862 | -57.97078 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5499518c-2b13-3373-a6f2-e389e3005acb | -3.98537 | -63.16001 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cd9ba6bb-0135-38b5-bb67-db40045cce2b | 2.08919 | -50.90522 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8afa293c-9745-3c52-8ee8-4e8bab566948 | -3.37878 | -59.42973 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 89f5e64c-ab31-3886-a205-02eacac9dc0b | 1.76863 | -55.6005 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f49e01d9-580b-31f3-b635-6a72e02740a8 | -2.78018 | -54.10059 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| bb56e914-3cac-3f06-a484-2e18a00e49c7 | -2.1007 | -56.62195 | 2026-10-05 17:17:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97af660f-802f-3161-9513-9df0d2cbe356 | -3.38286 | -59.42911 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 51826060-606e-36a1-a871-2a8795f396d6 | -1.78677 | -66.55293 | 2026-10-05 17:17:00 | NPP-375 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 406d3791-85b0-3117-9466-177c8030a708 | -1.49174 | -55.67029 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 079c09d1-7331-3c1f-a771-9b46cffe4702 | -1.6402 | -54.86999 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 136d7153-45c9-3533-a712-ed72be440925 | -3.32802 | -59.48146 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ec1d19a0-bb72-3685-9e77-dd872ca461d9 | -1.89039 | -48.5041 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1280a669-7fc8-3c49-9514-32d0f31cd03d | -2.27713 | -57.02058 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23c4b251-a1c2-3315-8f5c-bd4f00c7e976 | -2.92642 | -53.93174 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd4c6591-4b36-3ee2-883f-dcfdbaa2d6c2 | 3.52822 | -51.50663 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a6bfa11-40d1-3698-8a17-af9335443f00 | -1.20132 | -55.69112 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f61f605-e080-3ac8-b02e-17bade4b2e1e | -1.85384 | -50.63253 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fa33d4fb-a1f0-3a84-9c8a-c9393c9e6447 | -2.09522 | -48.83797 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e24aaa31-f4d3-37cf-9f54-7e727b0aa608 | 3.52117 | -51.50066 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 221ea783-41d4-3894-95db-4be6ad98205d | -2.96345 | -54.10645 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f1fdb52e-2379-39b2-9970-601cc0ea58f4 | -3.66838 | -59.66901 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ec1d939-a41d-306f-b7aa-7c0a91d0412e | 3.46805 | -51.53405 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99e2f1d3-339f-3398-ae12-8a4cd69a3e59 | -2.96211 | -54.14199 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 59b32bca-058b-327b-8330-0d6c182812b5 | -1.51936 | -54.80807 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f1eae6bd-967e-3baa-87bf-539b289fe3f0 | -0.71636 | -57.96997 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b2dab94a-95f1-3b26-927d-6804c271e9ea | -1.46462 | -53.59653 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17bbac41-0b9a-3551-82d7-dbb10ed07ced | -2.78056 | -57.68143 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README122.md)
