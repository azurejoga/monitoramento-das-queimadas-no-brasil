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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 041ca237-30da-32b2-9b43-f7d0e258246d | -14.76751 | -47.49954 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad252bab-fa0f-3cc6-9a07-d79734cc1d90 | -12.92628 | -56.95579 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 492ab631-5f91-3b7b-b899-c4001308c39f | -14.20972 | -51.65501 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec4b3ddf-3895-3916-84f0-b9de177b1d90 | -14.71347 | -46.7486 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab691783-8281-3d5c-a205-3f3d5f4fa08b | -14.79375 | -48.19705 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14614518-17f8-3019-ad71-f8f3184a960c | -15.57074 | -48.39032 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c73d0ee0-3c0c-36f7-b621-ef5a975e41d6 | -14.7981 | -48.21458 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b64aad4d-447d-3763-8289-61a121af161c | -15.10023 | -48.10872 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30333857-a7a6-368c-a5b0-70c1d18c7c51 | -14.59457 | -48.047 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75978c6d-4cee-3835-88b8-4489f7ed86c9 | -14.79453 | -48.21386 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d660640-aad7-3513-98f8-216ef099afca | -19.81934 | -45.00394 | 2025-09-02 04:17:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e4b476e-6cd9-38f5-9f25-41e3cf609e91 | -12.9157 | -56.94268 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee36ac6c-8e0f-385d-96e3-abe7f36de7f2 | -15.56869 | -48.33792 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cb6e8775-b1c0-3e96-9465-52163a323760 | -12.92409 | -57.00491 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d95d0d3-22bd-3e32-8572-8dae3429f69f | -14.75163 | -48.15273 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0476ad5-9339-353f-b4b9-55640b9729de | -18.85143 | -47.33818 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d1708fb-0e86-3b54-8c72-b5dc7fa2b16f | -15.78798 | -42.13321 | 2025-09-02 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb55718a-896b-3871-a790-8899445eed17 | -14.27079 | -45.24984 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2567b1e6-54e8-33f6-908f-f00598fd9b72 | -19.8576 | -45.2864 | 2025-09-02 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b15ebb1-0980-3479-9a6c-3ff5aaa8f0ad | -13.89193 | -48.11031 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1f65ca6-a859-35f2-a6c9-7f9b9a4f4550 | -17.2379 | -40.92372 | 2025-09-02 04:17:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dce8c4ff-2dfa-3a14-be5a-fc46151cc3aa | -13.89556 | -48.08894 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f12ca5e4-66ae-3d13-b69f-de16db31ff6d | -13.82113 | -49.38115 | 2025-09-02 04:17:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d3f33a3-773f-3207-ba03-c96b6366dd4a | -14.48948 | -45.94357 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a32b44c2-5cfc-3c8c-9db9-2a1d00081601 | -21.06483 | -46.349 | 2025-09-02 04:17:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| acbe6f8a-8c49-37a6-8922-664ba9bde179 | -21.11787 | -46.85087 | 2025-09-02 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 064d6f12-476c-3102-80e4-fcac7f934fdf | -20.69833 | -46.30466 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b7ad05-f82f-359f-a54a-582ba2c5cb76 | -25.09731 | -49.80204 | 2025-09-02 04:17:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34d6216c-041e-37ad-ba8f-023a86a460e6 | -14.79523 | -48.20979 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 347aec5c-a687-35eb-972e-7de1cdef0522 | -17.28831 | -49.20358 | 2025-09-02 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5c0a045-e805-3a06-901c-b425668f8bd8 | -17.28546 | -49.19838 | 2025-09-02 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc269a61-fe74-3a3e-bba7-141186fa429d | -15.55948 | -48.32724 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e5f4b57-edb4-33ed-858a-01f36b1d738c | -14.59529 | -48.04284 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae35ab21-4454-31fa-91fc-d5497e1f316f | -14.26691 | -45.25284 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fe921c1-8f6a-35e2-8f08-44a468961ef2 | -15.11385 | -48.18017 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa0ad4b-0d24-327b-861d-8b9ec4075d58 | -14.49557 | -45.94831 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bfde5d3-85d0-3830-a388-765a896330bf | -17.70353 | -46.8918 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8be66972-20de-30f8-afd4-cc5b765e8899 | -19.45473 | -45.30703 | 2025-09-02 04:17:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 394c969a-5c70-3b13-b782-fe16f0d69662 | -14.98894 | -48.32004 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea7333f-617a-3f4a-a80d-3104a3a60fcf | -14.81756 | -48.35971 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88e7b8a2-fb03-3393-b706-f5c02551b201 | -18.54824 | -47.45832 | 2025-09-02 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f298fa26-df67-3115-9e85-d916c3ab99f4 | -16.08132 | -43.62198 | 2025-09-02 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eda77156-c487-342b-8baf-77f0ef8a32ec | -13.89552 | -48.11104 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 885f2a39-2804-36d2-88a6-3abae2297b00 | -15.02507 | -42.14869 | 2025-09-02 04:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 744aec86-874d-32e9-8d7a-a0249c3ca40f | -18.04376 | -47.74605 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7284752-4012-3ce2-abbd-2da62a86ce02 | -16.80402 | -49.52399 | 2025-09-02 04:17:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6578233e-50d6-32e6-9458-3fcec362da6c | -15.72949 | -49.02865 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec8c8990-ecc3-37a2-bc9f-d8dfb2de8664 | -14.0713 | -50.15402 | 2025-09-02 04:17:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae7ac4f-b274-36d1-bd6e-edac03adc4d0 | -14.76958 | -48.15558 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c49e7a12-a7d4-306a-ac07-51891077fc74 | -23.93514 | -48.84972 | 2025-09-02 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0008357c-4552-37cb-8893-772db555e2d0 | -20.74625 | -47.1346 | 2025-09-02 04:17:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2d3d81-0670-3a40-8dd4-883bb5720b72 | -21.33722 | -48.73341 | 2025-09-02 04:17:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 17e9510d-efd6-3f49-a356-ad6a447ed8a8 | -14.73446 | -46.74829 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f325636-6fef-3632-a1ef-bbbadd6766b9 | -14.55507 | -48.95826 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca711ab0-0a5e-3d07-86ac-0ccd8847f513 | -13.7923 | -48.49316 | 2025-09-02 04:17:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19054221-011b-31b3-af77-90334d46e2b5 | -16.28847 | -52.9365 | 2025-09-02 04:17:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b8734f2-161c-36d5-b7b7-180366841be3 | -15.55649 | -48.34452 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7525081-abf8-3661-88db-f63f6ac653b4 | -16.59234 | -48.97443 | 2025-09-02 04:17:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88720bd6-5025-3553-ad18-7c89aca6d40e | -15.72866 | -49.0212 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70316f3f-d537-3451-a3ea-730ef005ce53 | -13.89413 | -48.09737 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da97428f-ec20-34b1-a736-771431f2e013 | -14.59451 | -48.06856 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f32ab81c-da1f-39ef-8d29-6a765b26682c | -15.73032 | -49.02402 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e0aa19-79e5-30aa-bf60-2d9aba12c27e | -14.21657 | -48.0554 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69fed99f-7dde-3a61-8823-f986ed2dabd9 | -14.60034 | -48.03492 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee39a920-50a5-3bd8-8605-e28e96acbf3f | -19.75752 | -47.89343 | 2025-09-02 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e0c262c-cf84-319d-8487-027f0d56a527 | -17.20514 | -46.06308 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42f3bc78-eb6d-3731-a7de-a0f23798e64b | -20.11618 | -46.01217 | 2025-09-02 04:17:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e87e780d-333f-3620-813b-17b59e443969 | -12.90077 | -56.95086 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a246f4e1-d3f7-3d8d-9098-50e79ab1e3e3 | -14.20528 | -51.65417 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c616559e-3cdf-3efd-a805-930fd659770a | -14.99613 | -48.14634 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41d6e95f-9bd0-34d4-b324-14d8a949258a | -12.91991 | -56.95456 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2eaf73b-e215-3d9a-95a8-2125670e7c16 | -15.55723 | -48.34026 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fe2ce30-b41f-313c-bda0-bab8dc20dc97 | -17.70748 | -46.88869 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9731b147-5fb9-3683-8244-a8af6ba74eda | -20.48649 | -49.69104 | 2025-09-02 04:17:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef13b38a-e988-3bf4-83a0-510eafdac752 | -12.92638 | -56.99403 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66c29556-cfc4-3d2b-8eb0-71379aa1e99b | -14.619 | -48.03322 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10231f29-4180-3142-98f3-00e4a3ce25a2 | -14.74064 | -46.75309 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6f8c437-4dcc-3da0-a639-a604620894d6 | -14.79738 | -48.2187 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.6 |
| e04ab96b-5aad-3fc4-a19a-ebff73411b46 | -15.55439 | -48.33536 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d47993c-9cf7-367b-9437-8acd2b8b1248 | -15.69282 | -48.92111 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c663946-695e-3530-9597-20e54172af2a | -14.59097 | -48.06775 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ca286d3-e4f6-3611-a940-4e1f7261624a | -14.75815 | -48.15773 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c2bd241-6370-39e8-b9e2-82d4d35de1e2 | -17.20183 | -46.0625 | 2025-09-02 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d39ffa9-9850-31eb-ba68-da3c27be6e92 | -17.23281 | -46.91998 | 2025-09-02 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef09aa69-7175-3ed6-855e-8effdfd9c7f2 | -16.85455 | -49.57051 | 2025-09-02 04:17:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17c102f4-b3bf-3f38-b86c-f2419a553dec | -20.83729 | -44.8591 | 2025-09-02 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c72e3c8d-205b-3863-b750-dac8678f4117 | -13.89485 | -48.09311 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48f3a519-ccca-3cd8-90c1-79e7ba938c55 | -14.595 | -48.0533 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e5da028-516c-3793-9f78-12cf29d1f7be | -16.4117 | -45.64826 | 2025-09-02 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19b5ac17-d09d-3f8e-8a77-a41d4389ba09 | -14.59569 | -48.07111 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c206087-43c4-346e-85aa-8d73c8d71fb4 | -16.59521 | -48.97953 | 2025-09-02 04:17:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee5d1434-6d9f-3dc0-ae68-9963f1d36349 | -16.86117 | -49.57676 | 2025-09-02 04:17:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fe98367b-05a0-3993-935b-964fbc945c4f | -20.06691 | -45.40479 | 2025-09-02 04:17:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e42e6115-65fa-3902-9dd9-939fb56ecbc4 | -20.74957 | -47.13521 | 2025-09-02 04:17:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b3ff0d-a809-302e-bb71-0537f184fbfc | -14.60135 | -48.03734 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46f14c46-9c93-32cc-9dc7-4e83d6d27eed | -14.25811 | -45.24408 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33b8ff3f-88a9-38e0-b31a-00bad1dc63b7 | -16.74061 | -49.37476 | 2025-09-02 04:17:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8358546-95fc-34ac-8c00-d670fbeb5382 | -15.55576 | -48.34874 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1afa34b7-c075-3b1f-9b92-5d91ccd3c3d0 | -14.58932 | -48.0652 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a3f9ef39-7b57-3e3b-ad26-509c4a634cb4 | -14.58554 | -54.56839 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
