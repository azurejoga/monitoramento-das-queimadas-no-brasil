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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af727feb-0c27-3f84-b7e9-78624f102b07 | -13.32202 | -46.84881 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cad2fe5-a908-3092-ad4c-f183070168e7 | -17.17123 | -46.08526 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a10eaee5-9a45-3140-bae8-a332f5a158d2 | -13.6918 | -46.92728 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a9bcef0-9dcb-3cdd-9b71-1f6cbd13dda8 | -15.72724 | -48.89462 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea85cc5b-c274-395d-9af8-78e83b7d9eff | -17.39148 | -44.9879 | 2025-09-01 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d4de955-baf4-35e7-b210-7771f9d8977d | -14.98715 | -46.70825 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7e52039-a99a-3f18-8b65-6e0d0390fa08 | -11.93197 | -50.62834 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dae51311-d9d9-3a0c-a735-f878d59f72f3 | -14.42182 | -51.66992 | 2025-09-01 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ac5b9bc3-ddb2-3fa6-9d67-db60a8b8ab5b | -13.69336 | -50.76921 | 2025-09-01 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb06c995-24fd-3649-a675-a2c4eb6e4ad9 | -18.11949 | -48.54312 | 2025-09-01 04:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5bf498ef-abb3-3820-aed0-9f4a2761533f | -14.75497 | -46.75354 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b5535e26-f3b2-3bdb-8188-7083eb8113bf | -15.60216 | -48.33281 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a71b9d8e-6deb-3d0d-9bb3-f2f7c01306f1 | -13.47693 | -46.93587 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7798a9f4-fa13-30f2-9429-9888a29f3a8d | -12.87797 | -48.09439 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cadb5654-6860-37fb-97cc-6360ae554318 | -13.32294 | -46.95526 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b862a0e-68de-3a8e-94d7-2377bfd2f271 | -13.47877 | -46.9935 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6c78d88-1205-3ebf-8f10-e152ab1fe93e | -13.37806 | -46.94854 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1909372-45e8-3d35-a3cb-50ab47dfa925 | -12.9691 | -48.11929 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a4d8551e-cd62-3f46-9f4c-1832e84cac87 | -14.76512 | -46.76018 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 875a6c44-b1fb-3dd4-b095-9fff2c786630 | -15.60031 | -48.34327 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0989cb36-31f9-3140-a16b-73c24b984ee7 | -17.8307 | -44.32383 | 2025-09-01 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91b33054-f65e-39c4-bb1e-fcecff07a445 | -15.72665 | -48.8941 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 453231ea-3ff8-312a-80a8-254d1c8ab77d | -12.38818 | -46.47227 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1080c1ad-ca67-3d77-8e1d-30d89a4a5512 | -14.84718 | -47.09167 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 624a14b7-3926-33d4-9c2c-3e88455bfd85 | -12.85289 | -48.07109 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5a9b3a3-fb55-38cc-be4c-b133c4616b56 | -15.69659 | -48.90149 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7d2f00b-634b-338d-b5e2-f4c824f3bbd7 | -15.59148 | -48.34718 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fed8b8b-0284-3425-b410-f4af9d327930 | -13.67046 | -46.93534 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 612e6931-acb9-3151-aed0-d0989443eb63 | -14.04798 | -44.57298 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6415acc-ba41-35ac-ab54-d44f31da5808 | -16.50602 | -55.0368 | 2025-09-01 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b99696e-beda-3cdc-8acb-b0ecfebc880a | -23.84374 | -50.70692 | 2025-09-01 04:14:00 | NPP-375D | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2a5f824f-ecca-3b0d-815c-a0356ed5b419 | -23.42928 | -46.80578 | 2025-09-01 04:14:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dca0e3a7-a160-328b-8baf-37e3c82fd89d | -22.45343 | -49.01364 | 2025-09-01 04:14:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d644b323-ec5f-3b29-99c6-93b5dbcd59e0 | -21.35172 | -49.0499 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 562d32f4-2ad7-3365-aa88-e2142a015768 | -20.40839 | -46.40227 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ed6609d-5be9-3db8-a056-a49be2901bf3 | -20.40028 | -46.40868 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a8cdb36-6e2a-38b6-9865-268baa5c503f | -19.69324 | -44.92681 | 2025-09-01 04:14:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dac630f8-0bca-31fa-9bf1-a54a0596283d | -23.5201 | -46.97555 | 2025-09-01 04:14:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e4432ed3-4ab8-3f01-bf9d-a717dd68cc08 | -22.44684 | -48.43048 | 2025-09-01 04:14:00 | NPP-375D | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63a906e1-1108-38c9-af4f-f3e9fb8c7526 | -19.47915 | -46.58643 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ac7c39f-30dc-396f-bd72-86f7c3b26932 | -23.35913 | -46.91238 | 2025-09-01 04:14:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fe4bc5a1-70c1-38d5-a7fc-fe2e6df9b0a3 | -18.65769 | -52.59672 | 2025-09-01 04:14:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90a953e9-bd8e-3c8c-8fdc-b37bee69b539 | -23.49548 | -46.91396 | 2025-09-01 04:14:00 | NPP-375D | BARUERI | SÃO PAULO | Brasil | 3505708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee859edf-d480-36ea-a1e9-3a56a8a0869e | -22.98765 | -46.22039 | 2025-09-01 04:14:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc4e8646-9569-3371-890a-c046d4dff33e | -18.65882 | -52.59114 | 2025-09-01 04:14:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bc89bd9-5e77-37a1-a3e9-586f20a5bfc0 | -21.09019 | -48.22453 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0a6cd40-6954-301b-bb3f-7f4f2fa814a9 | -21.35459 | -49.05546 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 982ce009-3899-3747-a8f7-7729db8e4721 | -22.37388 | -52.44402 | 2025-09-01 04:14:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 884244c5-9077-358a-93e8-751a7279d71f | -22.37836 | -52.4451 | 2025-09-01 04:14:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9de72583-5fef-367e-925a-661282a3cf53 | -19.4826 | -46.58705 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12e9c9f1-5504-343b-8f07-0c749c45501a | -21.08578 | -48.22825 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5ca9404-e071-31f7-b22c-b33743ae310e | -19.123 | -46.45274 | 2025-09-01 04:14:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5719fde-e18c-338e-af96-6406e865a0bf | -20.41265 | -46.41864 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ace73a01-bf8b-3511-b3ae-91ab54b4dcdc | -20.40512 | -46.42163 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dc1931f-d41d-38ba-b451-7f4810b6c86d | -24.20584 | -50.93776 | 2025-09-01 04:14:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43492214-de01-3d6d-b6cb-52ecd0a9b87a | -20.40436 | -46.40535 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4f8d807-c55d-3d83-9f92-50ea23e1ffdf | -23.73347 | -54.93869 | 2025-09-01 04:14:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 92bea373-d2f3-3761-94e8-f7b57ebeb632 | -21.87505 | -46.75071 | 2025-09-01 04:14:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3ad20ec8-042f-3e87-a151-c5f74d8e8965 | -19.34612 | -44.00054 | 2025-09-01 04:14:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22585a7b-188b-33a5-b120-61730165c34a | -21.35082 | -49.05472 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c1a8c9b0-1b62-3719-a286-dc0621823c67 | -19.34945 | -44.00111 | 2025-09-01 04:14:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b1e849-f31e-3124-9579-076e3998c0ad | -19.84188 | -44.99435 | 2025-09-01 04:14:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c09ef1-b96d-31ad-9584-1fdcb8f044b5 | -23.73849 | -54.94027 | 2025-09-01 04:14:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6c12ea0-bc40-382d-98ec-48a0d7570289 | -18.57241 | -48.35434 | 2025-09-01 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 57168223-f309-3611-9bac-57f10913f1ad | -18.66255 | -52.59785 | 2025-09-01 04:14:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 477abe18-c6e0-3f14-8f52-23a5e882985b | -22.9843 | -46.21976 | 2025-09-01 04:14:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a599e5c-5a54-3f85-bc57-e0f8fd548103 | -20.41199 | -46.42253 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 16611022-55c7-367e-ab0b-4b2ce95f563f | -20.80907 | -45.62744 | 2025-09-01 04:14:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8020f06-9e9a-3289-ac2e-b087a22802eb | -20.40922 | -46.41814 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b4a97c4-7df6-3678-a558-55f97d451a5a | -23.17503 | -47.11309 | 2025-09-01 04:14:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 97e3d691-a60d-32fe-ad97-6b3b232b2c38 | -23.80136 | -48.14731 | 2025-09-01 04:14:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6f5762a-48d4-30a3-bb1c-8b4fd4ae612e | -19.47847 | -46.59047 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c29b3a4e-091f-392e-aa25-e3226da530fb | -21.0886 | -48.23341 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0dec4c73-3ff9-3a62-a924-91bcd2db7a29 | -20.40855 | -46.42208 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 867fae98-d9ec-3a0b-967e-4111ec4f8ed0 | -19.48605 | -46.58766 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ca32c2a-d123-35c7-a4ab-50bdb44878c5 | -19.88185 | -43.85551 | 2025-09-01 04:14:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 53424ff5-3017-3139-a617-7e36dc86a561 | -20.11068 | -47.31544 | 2025-09-01 04:14:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| acd30d3e-f989-3204-9b62-9bb02a1e4afb | -18.65655 | -52.60233 | 2025-09-01 04:14:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9a26c40-600f-3e40-a695-1ae878168af6 | -22.5689 | -47.46983 | 2025-09-01 04:14:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ac29586-9f6f-38c3-a556-5f045829adf3 | -21.37154 | -45.52058 | 2025-09-01 04:14:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6421988a-0f56-3ac2-bc37-0ad7ed420d73 | -20.08673 | -47.32782 | 2025-09-01 04:14:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91163518-31de-37e2-a76a-63018e059a2b | -21.09143 | -48.23855 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e4d4df7-922c-3d7b-8f03-8227a2ebfe36 | -20.41053 | -46.41037 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4baaa4c0-7d08-3373-b035-3666ee601d2e | -21.08419 | -48.23709 | 2025-09-01 04:14:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9cdafa5f-7572-39a4-871d-31262d9a3476 | -21.35221 | -49.04786 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d26d1494-a352-3cb4-bd52-b0705087246a | -22.24877 | -54.88701 | 2025-09-01 04:14:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a701156-7e53-30ad-920c-f636e3b1c432 | -19.50814 | -45.31576 | 2025-09-01 04:14:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07d819a7-e2fd-364f-a8db-647587656bb0 | -19.12366 | -46.44883 | 2025-09-01 04:14:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f485e978-a856-344b-9eaf-220939b06273 | -20.80573 | -45.62682 | 2025-09-01 04:14:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44bee7d2-4395-35d7-8d75-d7b6cde6252d | -21.0894 | -48.22897 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9996bf04-80d7-399c-9e47-d29fda410ec8 | -20.19968 | -47.42956 | 2025-09-01 04:14:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 754aec87-27e5-3442-9052-f95d069a5bb5 | -21.73266 | -50.74298 | 2025-09-01 04:14:00 | NPP-375D | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3b6dc7ab-1725-3cc4-9d7a-8c31c9cac19e | -19.85952 | -45.01271 | 2025-09-01 04:14:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d7567b7-a802-3d62-8d54-147b1bf78a46 | -19.52262 | -44.10177 | 2025-09-01 04:14:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65de85a1-d62a-3f69-b239-d7162526043c | -23.43265 | -46.80644 | 2025-09-01 04:14:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| de98c379-5438-3163-bdb4-6531a0191936 | -19.84247 | -44.99067 | 2025-09-01 04:14:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22d61f0c-de41-3b02-80bb-292b7c575dfe | -22.36042 | -52.13439 | 2025-09-01 04:14:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e32998d3-e5a1-3110-8745-cda203869e5a | -20.40712 | -46.40979 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe9fa638-5a27-3aa2-936c-f200cb06044f | -19.97141 | -50.22235 | 2025-09-01 04:14:00 | NPP-375D | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ffe4013-145c-38d8-928e-46aeaeebd7db | -21.08781 | -48.23785 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README48.md)
