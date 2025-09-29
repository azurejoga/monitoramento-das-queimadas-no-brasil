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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1697cbcd-c792-3c0e-8312-c1bdd28ac75b | -13.83249 | -47.4918 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2800c5a0-1aa2-30ce-9705-88a917d770ed | -14.52007 | -48.40155 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2b76f0b-05d1-34d4-8072-5e0c7f018899 | -11.67272 | -44.29747 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb26280a-d595-388f-a40c-ce7d13c8ec9a | -14.57637 | -48.27259 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f47d1564-3f47-3ca5-b628-b5f920186bde | -14.54754 | -48.43267 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0c78294-3919-3528-91ef-5fc2fefbf9e2 | -12.97994 | -46.28682 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18d22b9f-8310-3c2e-b921-47124e9f9bd8 | -9.08213 | -47.63428 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e1d3ab-4aa8-3c36-9de0-d05d27c25a2c | -12.94571 | -47.18777 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2efa3c1f-c130-36cb-b4dc-0a59c442f5d7 | -13.16273 | -47.44347 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9287b0c-9ccc-373d-9caa-9a93f733272d | -10.73116 | -44.5594 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f61a8788-4344-30ce-a5ff-aee3b90b143a | -14.48941 | -48.5464 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e71a73f-0181-3897-a503-029cdd8386f4 | -14.5487 | -48.40331 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3184f14a-32f9-350a-ad58-10aa90c2f6ca | -11.81059 | -51.80503 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0bf693-29de-3f00-9a0a-6157512a40cf | -13.8118 | -48.01374 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9815b66e-7c4f-3998-b730-95239fa16605 | -11.93869 | -46.53834 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 392752db-2c1f-31b9-99ce-e5af942e4ce9 | -12.79566 | -47.76867 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e9273e4-97fa-39cf-9d99-3a705d12b19b | -8.71541 | -47.98037 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3c6196b-ec7a-3f4e-9fb7-0e37a6e7cbe5 | -14.48195 | -48.56421 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44ba522a-41f5-38dd-9ed1-569203bd696d | -10.42267 | -46.15254 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 874d094b-8653-3182-9020-778b67048117 | -15.87627 | -46.21925 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c64636-c7f1-38ba-b76e-3dc5488242ba | -11.86742 | -56.87712 | 2025-09-29 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a8c6459-8378-38e2-8f9f-8aaf7a02473d | -16.40359 | -43.7207 | 2025-09-29 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c5e40cf-d260-3aee-a457-78cd61e9ff07 | -11.35427 | -45.08338 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 460d14f1-35ee-342d-aa5d-7dd1de43e4fc | -9.65687 | -43.8577 | 2025-09-29 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3833e8c3-d8ec-3db0-a896-59fe897e5fe5 | -12.85304 | -46.98118 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8c4ba57-8922-3ef6-b0ce-42c24ec049f8 | -12.89652 | -47.09146 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c544b55-f170-3db1-b03b-1b94d5b5b70b | -9.27703 | -45.69411 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 757ee049-8482-327b-b707-b835351ab63b | -15.4386 | -48.20998 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b77f7ac-e758-35db-a6ce-632676f56db9 | -13.58433 | -47.29201 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48592e96-6d63-3adb-963f-586bce3f673e | -11.61882 | -52.85248 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ef34f76-635b-3a00-be7e-3abf654189f1 | -13.79227 | -47.87768 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7060467-3963-3f99-9e64-fdeb8be9c0d2 | -15.29276 | -46.4227 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a0816d5-0038-308d-85a9-80ef466884bd | -9.3095 | -45.70418 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5be38d91-78f9-3f34-8bb8-730e2371fb4d | -11.62447 | -52.85353 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3736f67e-af11-3fc5-aefc-a574ce4a556f | -9.77121 | -46.1953 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 535fc24f-28fd-3314-b491-befdb8c7389a | -15.90364 | -46.22793 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e5c8f43-171b-33f3-ad00-32893be6764a | -14.56638 | -48.25976 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b783759b-0020-3910-9513-a43962e2614f | -12.6555 | -51.66464 | 2025-09-29 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 107dc2db-232f-3c9c-9fda-f5a66d0f3f38 | -13.26412 | -48.44852 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efbdcddf-326a-3956-af08-91b5a6477f6c | -12.69901 | -46.90536 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f657321-74cd-3302-a86a-235f94df868f | -15.42433 | -48.24416 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 027739cf-f76d-3bc9-99e2-7e80a49cae85 | -13.60199 | -48.04788 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff9cb4db-7041-3a3c-9fd2-dbe2b543dc70 | -13.63069 | -47.31255 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48f3902c-487f-33e0-b3c1-aaf037696d37 | -11.81438 | -51.78556 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f4f1794-1648-3d80-93aa-173e1da1974b | -15.28988 | -49.51904 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0c0c76db-79f1-3665-85fe-38854a1c9cfc | -14.68014 | -48.1656 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde430ab-bf81-3568-bc2b-ce1ea025ac51 | -15.26298 | -48.75996 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91b0f330-01a6-30e7-81a5-d796ceecf7f8 | -13.82334 | -47.9726 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd261717-292b-3ec8-9188-1719e07e325a | -11.98386 | -46.58905 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| faf47fac-39fe-3986-9345-2f2d1b364830 | -13.76927 | -47.91596 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9bbc2553-26e7-3635-aeac-b8e6f5d63b4b | -11.37998 | -44.97078 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8863bab-d1fd-3250-9a6a-af48031219ad | -13.79633 | -47.94664 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e0316be-cbda-3144-9227-d9231a684c42 | -8.90888 | -46.08424 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fc4068d-3642-365b-89a4-a38178434dfa | -12.86073 | -45.18222 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c70d2f3-9aae-3a98-b26c-f0569b02db41 | -11.76006 | -47.565 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55ebcc1b-3460-3c70-985f-e2fdedaa4436 | -13.16744 | -47.44631 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885c3390-7af4-316d-add2-a5c2e7c46ab9 | -12.97772 | -46.29985 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90f08c17-b8d8-38e4-8869-a1a14401bac6 | -12.85545 | -46.96728 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95ed3fac-2101-3697-aa67-53635de49bda | -14.61804 | -48.29187 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a437ec3-443e-3ed3-a2f8-61d31bce7918 | -12.58664 | -41.28224 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6dd1e4c8-fc88-3de5-885f-4dafb8c79cf2 | -12.69959 | -46.90341 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 59535ef7-eee0-3030-a600-60b28a0e4fd3 | -14.58129 | -48.268 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9570dab0-4130-3a0c-8681-09347879c9ab | -11.43684 | -44.96 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ca10ac5-60b3-3a31-b0bb-4bf59c1262c0 | -13.82986 | -47.93656 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9eb2a10-1732-3b2f-8597-810f108f1948 | -15.53555 | -44.34855 | 2025-09-29 04:08:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a20b2d5-8f1e-3edb-9058-76f53e4660a9 | -12.27294 | -44.12059 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6cd9c6f-c776-387e-8a57-dca6eb030a73 | -15.54623 | -47.87507 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5ecb506e-af3b-34b3-9714-72efed2d0b07 | -12.58834 | -41.29383 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa9aac64-628e-3e71-b660-ca33f997087c | -15.4719 | -47.93727 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7d17e7b-221f-3ec0-a360-9a063aaa7f0a | -11.65303 | -45.33683 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53146990-9034-339b-b4af-bb9773bdf822 | -14.78872 | -45.69781 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0489376d-7fea-3558-a32c-37eba2e1ffb4 | -12.59002 | -41.28277 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d464e94-73a7-3713-ba76-418f5c1a2b79 | -11.40943 | -44.90012 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b9253f6-2285-33ff-9d7d-ebb9ee7d0703 | -11.41563 | -44.91601 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf7163dc-d827-366b-b8b1-a654810899c4 | -15.25611 | -48.77475 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8681791c-d292-3ce0-a54e-df2ec72ae41e | -15.2907 | -49.51448 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3f5448c4-a84d-300b-8b22-0dba00a41805 | -12.59285 | -41.28698 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2226de01-9e71-38c8-aeb0-4e9ef34b411c | -14.59465 | -45.01105 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6be247b-3377-30e6-9183-320393df1de2 | -11.86292 | -56.88199 | 2025-09-29 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 066d087d-c3c8-35e0-b4b3-58929e676c06 | -15.9105 | -46.20885 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b98ca46-c483-395a-a1f0-fdc4c16c283d | -12.70045 | -46.89858 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9271ee0e-32e0-3448-9d51-c9381d2c5e52 | -13.72313 | -48.6612 | 2025-09-29 04:08:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56ebf0ae-29e1-3f9e-b5fb-8764d6ece605 | -9.7794 | -46.93507 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 715d705b-5e00-3c92-aa87-33ea7b711254 | -10.81036 | -46.65932 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 729916f1-9429-3fe7-914e-aac9508cd2ab | -10.79186 | -46.68286 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a585617a-6f02-3a3e-ad26-4b3a4783b8d5 | -8.89411 | -47.62242 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38198647-6db1-3cee-bec6-fd83147ac0fe | -13.8081 | -47.90281 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d0dc1c1-59c2-3806-a845-cb3e42f157ae | -12.76212 | -47.77338 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de88b64-7537-3ea2-b4d4-01f1b0adc9ab | -10.69425 | -48.7461 | 2025-09-29 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7aae4380-e1a3-35ea-889c-5a1911b41824 | -13.73761 | -47.88877 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fe1260d-3a1d-3893-aea5-a69c58ba0484 | -13.76528 | -47.91556 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 732ba566-ecd2-3929-bfa2-4ef62ed3ff00 | -15.04368 | -46.96797 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbf7a945-7afa-3187-8bde-ad383723887d | -9.99285 | -45.42498 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1168e52-6e07-321d-92e5-5a89284f885f | -10.48344 | -49.36887 | 2025-09-29 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2e61c35-59f8-3ef5-a290-721ff2ab544f | -13.78929 | -47.87161 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f2afbc2-7655-34af-be47-de380fc8e346 | -11.4362 | -44.96386 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8d9aa0b-507e-3b65-a087-26455837e5d8 | -10.79649 | -51.97742 | 2025-09-29 04:08:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8d2b63f-be04-382b-a916-f65086f98291 | -15.53614 | -44.34494 | 2025-09-29 04:08:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 62e18384-f5b3-3d86-bfb3-e4469cd0d02b | -11.81117 | -51.80395 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bfac856-5ffb-3004-913b-1a2a87187c01 | -10.41029 | -48.11665 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README46.md)
