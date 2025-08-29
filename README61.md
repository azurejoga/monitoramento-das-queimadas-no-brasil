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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1082eaf2-529f-3379-9292-2fec8e59bb82 | -5.69429 | -45.95853 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da1d35e6-d746-330e-9cf2-83d0bf703c6f | -3.4269 | -49.04363 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e8d15f4e-4478-396c-b329-7f0a14d3a320 | -8.69012 | -50.39345 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6544035e-1557-382c-bd24-94cc15468d2e | -3.8477 | -56.97647 | 2025-08-29 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39714182-c0d1-3e04-b01b-95b8d3ec6b79 | -7.21539 | -45.44538 | 2025-08-29 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16230311-a0a9-3d1d-a39f-cafe774d81a1 | -5.61502 | -44.99759 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54713ab2-20f5-3b27-8f09-090f1e9cdb6b | -6.98993 | -59.34044 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98330453-6165-3561-a5d0-38f4f90e22bc | -6.3821 | -45.57961 | 2025-08-29 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bd918f1-da11-32c3-bb17-6783868c4713 | -8.69496 | -50.39007 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e25b9439-4331-3a0a-bf27-216541e0dfa3 | -7.73661 | -50.27035 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7818cdb6-1014-3e6d-a341-a1ad0a87b136 | -7.02797 | -44.67564 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d50556-85ca-3184-af10-5d88acad0e65 | -7.41159 | -43.38388 | 2025-08-29 05:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46e10c68-e8b7-39a3-961e-dd1ab113d342 | -3.98742 | -47.8831 | 2025-08-29 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97e69f85-c598-3cfd-955b-c3c2789ba05c | -4.48638 | -47.67924 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a01bd3a-d09f-335c-9317-3a8156cfdeb6 | -3.42043 | -49.04845 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 36cd934c-6421-3e6a-958a-e37b4254aa8d | -8.55889 | -51.31573 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9dcf0e4e-cce3-32a2-916c-56118a8ec608 | -4.48317 | -47.66797 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 042f6636-b7e8-33e3-9999-2e6dd18a7007 | -7.39475 | -45.93817 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4aa689ec-ab3e-3934-aa81-d946e933eaaa | -6.21172 | -55.66729 | 2025-08-29 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a299b89-a65a-3098-a7d7-0ce62f29537f | -6.876 | -43.61332 | 2025-08-29 05:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3b6a182-e94c-3735-af3d-f1316c660fd8 | -8.56425 | -51.31784 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b78b8f65-0124-3236-ae68-8b660a97b8cd | -5.62475 | -45.00537 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3076dffa-619d-300d-82ad-426eb2e7f2dd | -3.24197 | -50.8023 | 2025-08-29 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e205651e-856d-3ee9-8081-ff15a405d317 | -5.60282 | -45.20708 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf06f19e-90c6-3593-910c-2c1b195d500c | -3.42138 | -49.05112 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 951fa610-f855-3455-829b-002d404d4d10 | -7.3958 | -45.93065 | 2025-08-29 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 457db503-db51-3e11-9e79-0411be8e3ddf | -9.49688 | -45.39055 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d0e35d4-6547-3ed9-ba9d-a2d288ee1a33 | -6.48269 | -44.0938 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fd22567-c34d-3f55-a1e0-2ca8f8d144d6 | -6.21547 | -43.3323 | 2025-08-29 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2583ee-ea82-35ec-9c56-94c8603a5c59 | -3.98571 | -47.95816 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c581730-5b51-3e82-b8a9-a93dff35f996 | -9.49102 | -45.39552 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04078ffc-2af5-3c3e-9c06-3483b6091d7b | -6.54987 | -43.92953 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5e50dc6b-9fc5-372a-be24-e1e4176c41be | -7.15886 | -44.16103 | 2025-08-29 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0853da91-0c6f-3bcc-8826-b016c4c8ad07 | -3.60764 | -54.82167 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0c29eed-785c-3fa3-9911-f300068b7f85 | -3.75996 | -54.82421 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f7bed9e6-25d4-300c-884c-0a46deb09a9c | -4.07422 | -47.95327 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8844382b-fc74-37ac-8ac0-781f7c3e1736 | -6.97447 | -59.33103 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 068a33e8-cc20-3ffd-afea-06233ed2a89b | -7.02126 | -44.6791 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcba387d-b302-3aed-b7f3-e9ca2c32d1b2 | -5.69932 | -45.96296 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71ca38e3-6002-30c9-b69c-3983fbc0c483 | -7.0485 | -44.38837 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70876ad2-6400-32f6-932c-2ac358ef7c62 | -8.90502 | -47.32545 | 2025-08-29 05:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a92c63-54ab-3b46-911d-bf5e49cc184d | -9.49872 | -45.38308 | 2025-08-29 05:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba93fd48-a54c-3dff-b920-6ec7c11f47c0 | -5.78759 | -42.61019 | 2025-08-29 05:06:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dfc9c940-89a9-3b68-ba38-4bd867a3c6fe | -8.45454 | -43.71787 | 2025-08-29 05:06:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a11b7fda-8dd3-31c0-9559-25b5dfbb604a | -8.70876 | -47.8671 | 2025-08-29 05:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa6b17d4-821f-3eec-8153-fc50a61aeb06 | -8.43843 | -43.65659 | 2025-08-29 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91b2fdd5-8a62-35e9-8b20-253269ab89b1 | -6.26253 | -43.81143 | 2025-08-29 05:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5253834-7f2d-3a4f-9ab8-bb326148ac49 | -3.42171 | -49.04024 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdb9cba0-af05-3134-a5d9-9556712e6182 | -5.17835 | -46.07547 | 2025-08-29 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84dc2eda-d001-3fad-a4af-399663b82122 | -3.79142 | -49.42767 | 2025-08-29 05:06:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5dade358-7018-31da-adc4-73606f104f51 | -3.76437 | -54.81783 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8a9e9cb-e8f9-3442-884c-49287964d45d | -5.1838 | -46.07617 | 2025-08-29 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a719668-80cb-336f-a380-1a9322db6170 | -7.72159 | -50.28431 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcf0c355-fa91-35af-b04e-9f069fb244af | -9.69267 | -47.06203 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d35252d-9007-3129-9781-520ebba0d034 | -5.70483 | -45.96379 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5b7bbab-fb62-3d10-8d4a-7486b9a04aed | -5.62027 | -45.00277 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c85a07ea-351e-3d75-94ab-4cbe7da8f6c2 | -7.10676 | -44.59613 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c24bbf82-53c9-32cd-96f1-c5c143300778 | -5.61888 | -45.00448 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| af3a1527-0ac8-3575-a624-e6b5fa721a99 | -3.46631 | -59.31212 | 2025-08-29 05:06:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b181851-fca9-33a3-b3ab-233e55a15f56 | -3.90255 | -52.03663 | 2025-08-29 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45aff1ce-c31a-3da9-86e9-a0c338c7d7b1 | -6.38873 | -45.58551 | 2025-08-29 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f367563-ec72-3fbc-ab93-6b9353dd3200 | -7.05255 | -44.35869 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ffaabd95-b08b-327e-8305-bf5280629a91 | -8.29732 | -45.14224 | 2025-08-29 05:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 539d5b33-5163-35b4-bef6-1acad045ac8d | -6.34567 | -58.1787 | 2025-08-29 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89eb21bc-2749-31f0-9a5c-a055fabb38f7 | -8.70534 | -50.36991 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2394225-a78f-3f0f-b878-b7d9521cabf3 | -8.70479 | -50.37388 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4d73374-05d9-3d97-96f8-e160e2a13d3a | -6.13969 | -44.4306 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f38ebf9c-5edd-3592-821d-8924096ae967 | -8.43564 | -43.65343 | 2025-08-29 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23147a99-cee1-39f3-9a4a-681766a55561 | -7.04289 | -44.38295 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c57fa83-5bc0-3cf8-bf9e-10e22d5f49d8 | -8.7091 | -50.37419 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3acc124f-c3b8-37f1-b7d6-f4d27bd117cf | -8.69405 | -50.38855 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e59f4747-0e81-3d26-9bda-453e1cb8e166 | -6.98413 | -59.34158 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfb33c08-612e-3954-8830-1d3057ebd9f8 | -6.19656 | -43.32343 | 2025-08-29 05:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dda8d8d-22b8-33cf-b759-0e0fb5cb417f | -5.69982 | -45.95935 | 2025-08-29 05:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b429f031-e397-3f83-90b8-bbea457243db | -6.13454 | -44.4238 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1370db9-9beb-3540-93a8-6ea04d9db8cb | -4.41381 | -54.86265 | 2025-08-29 05:06:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0654ab3e-a4c6-3669-b695-bb6726958903 | -9.42748 | -47.64201 | 2025-08-29 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a0a878e-ac01-3d86-b4a0-a97f6f820995 | -5.33318 | -51.33046 | 2025-08-29 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59f5c0b1-0284-3bf0-a22f-0c4f0104e034 | -5.18428 | -46.07285 | 2025-08-29 05:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f24f37d9-75ca-3886-a0a4-17bd3893113b | -7.05213 | -44.38914 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d166078-f67a-322f-b814-c6b1278adb30 | -8.55092 | -51.31433 | 2025-08-29 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1c29bec-5a23-3c33-81f9-7ed45fd3ed8f | -6.54482 | -43.91885 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a6e73428-5e56-3aba-b2c1-a19bdc9a0c43 | -6.8902 | -44.4463 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca8f9651-8aa7-3f52-8469-5b23ab137c0f | -2.90095 | -51.48054 | 2025-08-29 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 131140bc-a042-376a-91db-697e418ecc3e | -7.72835 | -50.29716 | 2025-08-29 05:06:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66c86829-6a62-3681-9a43-11e84e405729 | -6.99151 | -59.34282 | 2025-08-29 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12de0ee-e624-3bfb-ad89-a9ee725847cf | -6.70987 | -49.4577 | 2025-08-29 05:06:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27647dd0-7d15-348c-a04c-4b005ff80ca7 | -6.43684 | -44.57782 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c84675a-ccd8-3b39-a432-0038c6b9b3c7 | -6.48204 | -44.09866 | 2025-08-29 05:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 176855ce-111e-3f90-afa6-5d6a1e23f294 | -7.22151 | -45.31303 | 2025-08-29 05:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6461cb5e-c711-3aac-b75e-77105b096442 | -3.76328 | -54.82473 | 2025-08-29 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0bc2af8c-97d5-3264-b560-c797c9b19283 | -9.69314 | -47.05854 | 2025-08-29 05:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2f63fa0-2a68-3d2b-8778-5105e84b7098 | -5.6185 | -45.01497 | 2025-08-29 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97765a45-a785-32b5-85ca-fd5f4ba1e36a | -4.10996 | -48.01759 | 2025-08-29 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd4b874c-478f-388c-b19f-2397dcffbccb | -3.73746 | -48.94061 | 2025-08-29 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a791ad16-f007-3a63-a208-073467ca043f | -7.22064 | -45.45051 | 2025-08-29 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c08986bc-19b2-3acb-8d41-0e012f188a7b | -6.43127 | -44.57533 | 2025-08-29 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a487e2ea-aec9-3a59-8b40-64e7cd1c68ae | -6.49205 | -43.53016 | 2025-08-29 05:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af22d9d2-fbab-3ca8-9763-0f2e93e9dc1c | -8.69999 | -50.37709 | 2025-08-29 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9036e17e-e72d-36f8-b34d-85f8b3179b88 | -7.04987 | -44.37831 | 2025-08-29 05:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README62.md)
