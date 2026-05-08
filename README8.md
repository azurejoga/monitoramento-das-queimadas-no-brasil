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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2000d0de-9223-352f-a552-8eb2a135bb07 | -14.31495 | -57.73563 | 2026-05-08 04:49:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cce4137-d63e-35e3-933a-0cd485462601 | -5.78557 | -45.12595 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7024e593-8b9d-31a5-859c-d26a3e481c70 | -14.31928 | -57.73649 | 2026-05-08 04:49:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66cb3911-d20a-3c20-a304-6bb739e2d292 | -11.8416 | -57.84677 | 2026-05-08 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75abfa9-698d-3f0a-b5ec-1841e8ed01c2 | -13.48006 | -48.91521 | 2026-05-08 04:49:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c7da89-fde9-335c-97b5-f461579206b5 | -11.55365 | -48.27264 | 2026-05-08 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf7d7977-c26a-345c-af56-45fa259c5d82 | -7.34064 | -49.78909 | 2026-05-08 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc1accae-5c8a-34a3-b213-990e9b9158fc | -12.34806 | -50.02345 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bed0805-e45e-34f4-96d4-55020fa986de | -6.98622 | -47.69559 | 2026-05-08 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4acf485b-ddb6-315b-a016-86f23a7fb3a2 | -12.34751 | -50.02705 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69e30bd9-72ac-37ab-ab58-d9ca8893a7da | -16.15177 | -58.48975 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3ca194a6-5f4f-30a6-9a2c-d1120e46d9ad | -11.63308 | -47.88382 | 2026-05-08 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 480d72fb-6d71-3a25-980c-66ebd997da07 | -11.6437 | -58.25703 | 2026-05-08 04:49:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44c6c6e3-8b53-38ec-8330-57253db8e74b | -11.82458 | -47.34106 | 2026-05-08 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6e53155-2e2c-3748-af24-961c1abf596c | -12.86097 | -43.75706 | 2026-05-08 04:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0b24467-ad12-3a5d-9faa-f655efee4a24 | -12.34695 | -50.03064 | 2026-05-08 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 690be4e6-8fc2-3222-9daa-80c58d5d708f | -21.70829 | -48.41677 | 2026-05-08 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e471d9a3-a0a4-3a3e-a6cd-c25325c521bf | -20.2184 | -46.83611 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c0f7a892-8dfb-36aa-b11e-57bac9b7ed35 | -20.21503 | -46.83363 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b32a1bb-78f5-3629-aee6-15f605f009bb | -18.49677 | -55.49643 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4b9d7ae9-4a38-3fd8-b465-8f6b1b635f0e | -18.43545 | -54.70742 | 2026-05-08 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 861786a1-839b-3ddc-8097-f5f8d089e9ff | -21.70436 | -48.41622 | 2026-05-08 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d547b41f-3275-3046-b04c-4eb989c0bfb2 | -18.50525 | -55.51132 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e0d128cf-dd0c-3148-ba7b-762957cc3545 | -20.22314 | -46.83261 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adf00a95-99c8-3fe9-9937-b7dd8e02d2ac | -20.21794 | -46.83997 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3fd44047-799d-3264-8cac-186902ce3c35 | -20.214 | -46.84169 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c4118ca-5f23-3749-8a4d-83abaf718436 | -19.64184 | -51.10244 | 2026-05-08 04:51:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f99bab93-c378-34be-af69-8fa4621106b3 | -20.21887 | -46.83224 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 195d3355-e1ce-376a-abb8-6179be68316b | -18.50375 | -55.51988 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4324776e-f59a-393f-a7f7-af9ec0144ac3 | -21.85171 | -50.35543 | 2026-05-08 04:51:00 | NPP-375D | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6d5f5781-8dd0-30a4-b5a2-34d8350e85c3 | -21.03228 | -48.94241 | 2026-05-08 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e8768f1-a390-37da-8128-22d7a8a1b0d3 | -21.03292 | -48.93757 | 2026-05-08 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b1e4190f-85e1-340d-bb20-fc8d31a3cec5 | -18.51242 | -55.5127 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 45e11d04-d50b-3a72-8411-bbd356a64303 | -21.70759 | -48.42213 | 2026-05-08 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de6b158c-7837-3c54-ad97-45607b7c0ef4 | -21.4312 | -47.06253 | 2026-05-08 04:51:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9efefa2-9adc-3f0f-9508-4f8185f72ee5 | -18.50959 | -55.50773 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 624ea4c2-99b8-3c33-96db-3f61105447b5 | -20.22363 | -46.82862 | 2026-05-08 04:51:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfbd44e4-01fe-3fb1-b8e3-1ba283101dae | -20.72162 | -55.17373 | 2026-05-08 04:51:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e90be80a-79aa-30ae-9165-86bd23b8991a | -18.50035 | -55.49712 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef73e911-8185-31d3-af41-6265fa015cdc | -18.43892 | -54.70809 | 2026-05-08 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 414b88da-31c8-345e-bdc2-6d07184e4c0a | -19.70021 | -50.68068 | 2026-05-08 04:51:00 | NPP-375D | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20fbe3be-a53f-3219-81c6-9b399e7bda38 | -21.84875 | -50.35058 | 2026-05-08 04:51:00 | NPP-375D | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 83a7c972-b4f2-3983-9e52-e7f1cd89072e | -21.84815 | -50.35486 | 2026-05-08 04:51:00 | NPP-375D | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e626cfd1-7724-3993-a64a-b53081c43d9e | -18.50884 | -55.51201 | 2026-05-08 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| efcc01b3-164e-37cb-b1b3-7cdb41c0ffc0 | -21.70043 | -48.41565 | 2026-05-08 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 095a071c-747b-3aeb-90eb-a421d96f4e2d | -20.07727 | -45.35973 | 2026-05-08 04:51:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd6c649-2705-3eea-8cf6-aa6890205614 | -19.78077 | -54.4339 | 2026-05-08 04:51:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 444774b5-d42a-3516-beb4-632a621010fc | -21.84519 | -50.34999 | 2026-05-08 04:51:00 | NPP-375D | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ccffad7b-f85e-3540-bcfa-eccbf203d0d0 | -21.85232 | -50.35115 | 2026-05-08 04:51:00 | NPP-375D | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6bbcefa-63ae-346b-ac56-bda4692afb63 | -19.64241 | -51.09858 | 2026-05-08 04:51:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e8f1cdfa-0d55-3a8e-aff1-99560dce7f95 | -7.34029 | -49.78767 | 2026-05-08 05:06:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 471ef5e5-a463-3c5d-9ee7-9bae2a4dcc0b | -7.29256 | -49.62606 | 2026-05-08 05:06:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f16f2106-52c3-3673-867b-6383fa0cb388 | -8.36376 | -48.07726 | 2026-05-08 05:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aa9f6c4-e371-3d02-8bd0-844d9cb1ecc1 | -8.79031 | -44.8334 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5be4c970-3673-3557-ac34-2bb5086a54f1 | -6.98663 | -47.69506 | 2026-05-08 05:06:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9ebaf7c-78e4-302f-ae8c-6c88e0294e14 | -8.78974 | -44.83786 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10306f2f-31a8-3740-8160-aa8185cee167 | -8.78478 | -44.83539 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 461dd9b2-d3e5-3ab7-99e6-e4854f41c708 | -7.33761 | -49.78638 | 2026-05-08 05:06:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 660b2933-66e9-3c5c-af17-96197a905ee5 | -8.78355 | -44.83717 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44d556be-ee14-3c94-9ef8-af020c84842b | -8.78419 | -44.8398 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b17f987-86ca-3155-a1a8-3d6cffbce19d | -8.783 | -44.84155 | 2026-05-08 05:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1465a955-64cd-38c3-9f31-ad05fe189b79 | -10.04278 | -51.66069 | 2026-05-08 05:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a27a80f-7e2b-3600-a07d-ea2852315c30 | -10.67424 | -49.69217 | 2026-05-08 05:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eddf36b-25e5-3f4c-80a3-7336ede85b92 | -8.69144 | -49.09519 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 107e4600-6776-32b0-9696-42085c8685a7 | -11.47495 | -52.91716 | 2026-05-08 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5e06d43-16c4-343a-bfe1-149ee7b7d3ed | -11.47118 | -52.91661 | 2026-05-08 05:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e7522a4-6714-3e96-a621-cb03fcc9c02b | -9.69963 | -54.40322 | 2026-05-08 05:08:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95dc2682-d830-30c3-a518-05917aeff2fe | -10.66965 | -49.69154 | 2026-05-08 05:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fe96eb0-485c-37aa-a550-4dcac156ab19 | -8.6868 | -49.09453 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50e7fbcb-07c3-34a2-a257-391ce3805488 | -11.07118 | -52.47301 | 2026-05-08 05:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa1981b7-2f56-36a8-b6dc-f4e878bf1608 | -10.93403 | -49.43533 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2193a8-18a7-3dc9-b8f9-0303ceb6fcaa | -14.13506 | -45.38523 | 2026-05-08 05:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fdf07d6-93b6-373c-a897-ee8cc2668f84 | -11.84253 | -55.01728 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f10e05ca-aac5-3786-96a4-e772d0677403 | -11.79606 | -47.09589 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d9aab5-1478-32ac-a479-4ef5071a12c9 | -11.61473 | -54.17972 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a1fa272-3a38-3ff3-b4c8-2d35581c1d07 | -11.80118 | -47.10028 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3ce9af9-54b8-3ca2-b81b-48c42a71879c | -9.3001 | -48.58037 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3185ae28-d87f-312b-a2ea-7741dcfb3b0c | -11.765 | -43.6521 | 2026-05-08 05:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ba770fa-eb3b-32e7-b08d-e57c9ca7d134 | -14.17525 | -52.88621 | 2026-05-08 05:08:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2cd4fc0e-cd70-314e-a188-a1056bbd7f3e | -15.61439 | -46.52197 | 2026-05-08 05:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3065d07c-2e88-312e-94f2-2a2d09fc0845 | -12.18172 | -56.4468 | 2026-05-08 05:08:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3f3a558-8f7b-3c8e-956c-c258f5e451ad | -11.55364 | -48.27356 | 2026-05-08 05:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bda71e3-ec4d-3b99-8ee4-01595093ae2f | -9.25001 | -60.33462 | 2026-05-08 05:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63305e45-e651-3620-9da9-2d93c22e71e4 | -9.29524 | -48.57972 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1dc4fad2-03c6-3d2d-b7b8-67f249e9408f | -10.93988 | -49.44296 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96310868-7213-3fa5-adce-fae204af9a33 | -11.77264 | -43.65149 | 2026-05-08 05:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d5747f1-aeeb-34b0-a442-83dcfc1d186e | -10.23779 | -52.22848 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfd3f2b5-01c3-3ae6-a9e3-73ead32d76ea | -13.15329 | -56.8102 | 2026-05-08 05:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afbe82eb-6a16-3243-b451-652c8dfa0139 | -8.69212 | -49.09036 | 2026-05-08 05:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 331747e2-69df-36f0-b3aa-37bc5e6c4fe3 | -11.8448 | -57.84336 | 2026-05-08 05:08:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6328a8-4ae4-30a5-8b09-7126d676eb4a | -11.91843 | -54.10278 | 2026-05-08 05:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3702dc1-9d28-3ce3-9eb8-6cb2e3bea705 | -11.85053 | -55.0108 | 2026-05-08 05:08:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c124701b-7b74-3f46-847f-4e570e040e6c | -11.64796 | -54.39627 | 2026-05-08 05:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9121f59d-86e1-3a4b-9060-2ddf8bb5e10b | -12.42501 | -54.21532 | 2026-05-08 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a132024b-c76f-3185-9ab1-95acab4b040f | -12.12264 | -54.67038 | 2026-05-08 05:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a365e9-51c7-32b2-949b-f2c0e0d06bbf | -12.30477 | -57.40986 | 2026-05-08 05:08:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f18a7b8d-7f58-3ab7-84be-d25b54258261 | -14.20158 | -57.42064 | 2026-05-08 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 861f3165-1f07-3617-a2b8-a1bb248e5e8d | -9.3091 | -48.58693 | 2026-05-08 05:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fe777275-b002-3011-8240-0d2c521a6369 | -10.93736 | -49.44581 | 2026-05-08 05:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 493a2ce3-202f-3bcd-8a13-555b8c3bacda | -11.80209 | -47.09278 | 2026-05-08 05:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
