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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92252141-c19c-3ca6-8f29-d594686fb68f | -14.5352 | -48.42019 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ff47793-fc31-3b8f-b173-0331b61fec63 | -12.78161 | -47.75709 | 2025-09-28 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64d5651-a836-353f-8cae-a9e7fcd3912f | -11.85676 | -48.23721 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d80ac59-2f61-3562-94a0-864657e0ae6e | -12.01286 | -47.95778 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdd0552c-9e80-3dae-a718-e2060915bf23 | -12.32239 | -51.51559 | 2025-09-28 04:06:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69e93eca-63ab-3742-bf47-cd89ff8a95a6 | -10.4212 | -46.1603 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 394f9d3b-9e96-392c-a1c6-33104a9ecfc5 | -12.92894 | -45.15967 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c06e4d4f-b355-3bf2-aaf5-ee816cf9428c | -15.42452 | -48.22782 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80f9bc76-68aa-35b6-a696-3c7fdbf16e62 | -11.98311 | -48.01009 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a953fee4-e632-3639-aee6-6724f57fd602 | -12.00936 | -47.96748 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 271856c2-ee65-32aa-b0b2-5ce597ab1fd3 | -11.44316 | -44.9809 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bfe04194-84c8-3948-ba65-cd4484881bd0 | -14.5405 | -48.41642 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30c9a228-7f3b-3676-a35a-a7482396f505 | -13.64412 | -48.06935 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e5f79db-4f06-36c7-98bd-05c3ad307c56 | -13.50286 | -39.91261 | 2025-09-28 04:06:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96a329d2-f930-360b-8375-506e70a6996f | -12.97811 | -49.43218 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f90dbd-afcd-311b-be6d-7d2b8e35e4a2 | -13.34917 | -47.29687 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aabccddd-614e-3ac5-9502-9a7e1873ee5f | -13.02257 | -49.46383 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dace2067-adbc-35eb-8ded-2670ef13b77f | -13.37814 | -47.92345 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f668b140-9761-3132-85ef-cbf0d9121ea3 | -11.71931 | -44.42717 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe3fba5-be4b-3194-8c13-4f1ea7bfde6f | -15.43319 | -48.21426 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c6f2216-5cd0-398e-ae28-6ff827316db3 | -15.20499 | -44.0046 | 2025-09-28 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da80fb4d-1487-359b-8642-d65bd2f7d7bf | -14.76689 | -45.65764 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93727971-7383-3db0-b4f6-9e9541174a7e | -12.98021 | -46.84969 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f21dfb2-db37-33a0-be71-ba00095f9845 | -11.95145 | -47.92899 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1223c330-cb92-387f-8d35-c72851f4f1db | -15.4355 | -48.21636 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78179047-f7c1-322d-9f60-243f5c7fdda4 | -10.85695 | -47.79366 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d09bd263-a055-3f4c-907e-7ec590af1724 | -15.21437 | -48.0722 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75a23c8b-0305-32c0-8f4c-60f6394f943f | -12.69648 | -45.4758 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b91433b8-8f36-34ae-8d75-1d5dc9c50944 | -12.67897 | -46.88409 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87f78557-ede6-36bd-a824-5065da5f5be4 | -12.9737 | -46.28843 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6266b1fd-9e44-323e-8407-0236f6dfd04b | -9.45328 | -50.89771 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e74f0b-5e01-3aff-904a-fffdb67d409d | -11.3689 | -44.96309 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc0423e0-fca1-3732-b582-46a7a2486ad6 | -14.40327 | -42.48666 | 2025-09-28 04:06:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92836a03-c2ae-3a22-983d-b6d23b92f9d8 | -15.46572 | -50.2312 | 2025-09-28 04:06:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85b9a29c-0b94-3be9-a997-e4c4185ec476 | -12.98087 | -49.44416 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dea1dcca-224a-3519-8969-ea2226e40790 | -15.54677 | -47.89039 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fd35756-9858-3387-8a21-c2dc5ad2aa28 | -11.36382 | -44.94785 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8252beed-4f89-3a76-83cf-fdae88da54f5 | -15.28908 | -49.48609 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f66e878-781a-35f7-9ec3-d29e879e069c | -14.54855 | -41.65978 | 2025-09-28 04:06:00 | NPP-375D | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cccc3e56-c0b2-3ce4-8986-37ffc730e67e | -12.01433 | -47.88816 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07587204-acbb-327a-ba79-0b287dcb7366 | -13.75448 | -47.88585 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8300c154-c270-3515-8810-a460bf7183d7 | -10.91823 | -45.72822 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c78a47c6-6251-35ff-9fa6-0261abc9e246 | -13.76746 | -47.87003 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5002acbd-d073-34ce-8196-8a3e771f39d7 | -14.20451 | -44.60116 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af03b4d5-9fcb-3436-bd1c-6006c9d587fa | -15.58243 | -42.41096 | 2025-09-28 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b28d84ae-2309-306d-9be1-eda1c5a6acb3 | -11.79826 | -44.91576 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a872460f-9ba8-3d7c-8d9b-0ffc464650c5 | -11.97861 | -48.0092 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 207b8360-2490-3e3c-b6c5-c711c5e3ca2f | -12.95273 | -45.15476 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac8aea5d-e987-31c2-aa29-c34bc92e3f66 | -12.01108 | -47.90625 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bce8dd78-62e2-3a04-b857-68a1ca490884 | -15.52983 | -42.33956 | 2025-09-28 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba15106a-742c-3393-9ca0-8a86780c6c93 | -13.71513 | -48.34377 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9d02575-b57a-3526-ae33-02157fc06f3d | -11.65337 | -48.26912 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6cbd7c8-778f-3c85-b08b-79024435669e | -12.69277 | -46.87851 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16bc1d15-b6de-33eb-860e-7cb6a9246eb9 | -10.75225 | -45.39311 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3fa4c29-24b2-3e6b-9a60-b42dfa33e282 | -13.71072 | -48.34266 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3dd81a5b-811c-3a77-989c-585c6adb7fb6 | -13.79697 | -47.92815 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c1dd15e-fe16-36a6-9d16-fcc06d136926 | -10.45863 | -50.85426 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ddfa6ee-a362-3541-bdfe-f2bf636dd04f | -14.87838 | -47.98744 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dceb7f9-7521-3213-9e88-c7a30911fdc9 | -15.20266 | -48.47686 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 283134a2-e4db-336c-96ea-6cf7dbb328e9 | -12.00564 | -47.08595 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8adfff44-8543-3dc3-b405-c389b6c9f0d7 | -15.21165 | -48.06297 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed6483a6-6b60-3212-9a2e-9b6a9a0386f1 | -11.39121 | -46.9883 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a8d93d7-1f97-3544-8a50-267c90f7029b | -15.27878 | -46.42372 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc73943b-20f1-305e-89d2-af713806a71b | -15.43623 | -48.21239 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d335c19b-348c-3aa2-b814-a07bf1dd27e5 | -11.3905 | -46.9676 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dc31699-7edc-3776-b693-5c11cb1d1e9f | -11.58764 | -54.48683 | 2025-09-28 04:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 966ac062-6b5d-357b-97a3-897c79c4def6 | -12.10941 | -44.1955 | 2025-09-28 04:06:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ed21c5b-be93-3ff9-94ed-6d34d8618c65 | -11.94445 | -47.94186 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ef7d204-55fa-360d-85ba-46ed3ba59507 | -13.29118 | -50.69421 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fea0f19b-e490-3e0b-919b-d81e37d3bc76 | -11.39263 | -46.98027 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c7c84b1a-78ca-30da-a43e-27173f56b477 | -14.20522 | -44.59698 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 540a3aad-ad1c-3960-aa45-fa70b5ab3177 | -11.62362 | -44.42034 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f71e041e-4eb2-3d13-9120-5c8cdb78cc67 | -13.57042 | -48.28028 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64ddf3c4-b653-3deb-b6dc-16d0987f9a95 | -11.99446 | -47.05104 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b33808e-1de7-3b09-818e-7251e73fb912 | -12.95519 | -45.14923 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37469d8-5570-3ac7-bc68-a3126739458b | -12.29735 | -45.64079 | 2025-09-28 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 756c4f57-23c3-3940-bdd8-6084d4c2c7a9 | -13.62618 | -47.32214 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a488853f-342d-302e-809a-b593a2563d20 | -11.9938 | -47.95089 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 280ded06-3b0d-362f-aa15-1b458d38d5e9 | -15.44283 | -48.23384 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6eb39037-d1aa-3c44-b8d2-d89bef0fd8c1 | -12.21633 | -43.74866 | 2025-09-28 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff0e602b-4dcd-3a4f-9956-316a6e1f4df1 | -16.40334 | -43.71832 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a318f94a-3fcd-34c6-a5d7-7e98ba5c3e7f | -10.91732 | -45.73337 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c58ddade-2989-3084-9053-973b49ac61e3 | -11.35514 | -44.99768 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41c5e152-4bbd-3139-8620-bf88da2a38d1 | -12.99072 | -49.44543 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 254365d9-9f21-3ebf-a034-f7dd731a4c54 | -11.36305 | -44.95227 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d83a5419-e588-3734-a01a-2df19ce19e22 | -10.04502 | -49.2024 | 2025-09-28 04:06:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6993b8f4-7dd2-386e-a17c-fb4be1dc9c8c | -12.00745 | -47.90078 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a794662e-60b7-3da6-8047-3c187f038e73 | -11.43495 | -44.96101 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb9fc24a-45dc-300a-9c9d-7c961bd61739 | -12.29023 | -44.06056 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b5393c6-b2e8-35c8-8237-93ce4f602061 | -12.99939 | -49.45292 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cdeb0d8-e777-359c-a66c-bc437fed04ad | -15.15168 | -46.41748 | 2025-09-28 04:06:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0c9e2b2-4082-399f-a759-019d6128a24d | -10.05007 | -49.20329 | 2025-09-28 04:06:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6a5666c-b862-3d3e-9ac8-981ab0984fe1 | -10.58808 | -46.27375 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f09a6e-289d-3441-a6db-9ea1777d0d66 | -15.05962 | -42.33801 | 2025-09-28 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5c27dae0-0e2e-3789-bd31-1ba3176dd56d | -11.60104 | -44.33322 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5693c5a-1d64-39d2-b2bc-00a479a555b4 | -12.64566 | -51.66383 | 2025-09-28 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea8c6960-6189-3762-b75d-06dec0f2bfb8 | -12.23869 | -46.75618 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227459b5-bba6-33fd-b679-5c0605f8aca7 | -12.9758 | -46.28678 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 76a911e6-5897-3baf-b4eb-ef67cabf634c | -10.13285 | -51.6254 | 2025-09-28 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 560e0ee2-2f1d-32ea-beb0-7fb2c04e5212 | -9.89438 | -49.1245 | 2025-09-28 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
