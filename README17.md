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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea98e861-1035-383f-b3ee-8701f45d5ca7 | -13.23193 | -47.06734 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69714d8a-8433-3e9f-a077-29b24a05f05c | -12.15978 | -47.69985 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5110f96-8e15-3449-ab6b-ca5f2450ed0e | -13.88447 | -48.45929 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc1ca093-144e-3e43-87e7-f9ce7694e24e | -13.69876 | -47.68757 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b90c6c4f-28ed-3ea0-be6f-14729249d1f4 | -14.25932 | -48.12238 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b5df278-c4f0-3daf-9af9-89ef8b027bc8 | -9.80752 | -47.7555 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 405c9f77-07a7-32ce-88e1-2c6b20f7d706 | -9.80179 | -47.75779 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e170441-82da-3d2e-a819-9a3d3f3482cd | -13.69619 | -47.67493 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1ea307d-8777-3fbd-9e9f-aa7222759049 | -12.00854 | -46.77773 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f729073f-4ddb-3ecd-982b-b716a6c9fea3 | -10.76372 | -47.89244 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eb1b0ec-4974-3323-a1db-8344ece3a9f9 | -10.87154 | -44.41018 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3895af1-9dd7-33cc-894a-103b5a43b83f | -9.11578 | -47.6516 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a802963-6e4b-3f97-af14-41132cb0ae69 | -11.99929 | -46.776 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 58c60530-7bc8-32fb-bcb9-fdeb599ff0f9 | -13.35512 | -47.38949 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a19ac064-5ee1-33ef-9f5b-1ef4f2496215 | -14.30635 | -46.53629 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b6d137-3957-36c5-8001-404392a879e3 | -13.2106 | -47.05377 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbe3a3d6-367b-3322-be5b-f7ff46b8d726 | -10.75356 | -44.75293 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5df05e4e-a2f8-3d2a-a24f-8e7dc1398115 | -15.15684 | -47.2327 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87725fe7-a761-3406-8c5b-0b368335bfc4 | -10.22593 | -45.93847 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1a7ecf2-ff97-3289-8e90-f922f7dbc5eb | -9.93068 | -47.67662 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c580cee-f2c0-3b4c-8427-d76893642b0a | -13.89668 | -48.50435 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ebb481b-3fd1-3d76-90c0-ee869c5572a2 | -8.51261 | -48.27754 | 2025-10-29 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f4ca81-a065-37cc-9ddd-b81d40023be7 | -9.94855 | -47.16185 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1015bdef-f973-37ae-9e45-424280e3949c | -15.96136 | -42.30898 | 2025-10-29 03:55:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec57d4bb-c5e6-3b68-80de-95ac0c50379d | -9.92668 | -47.66988 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef327c37-cd80-3ba4-babd-d3de914c0417 | -13.69412 | -47.68595 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ff99d4c-4358-30de-9e6a-b7c0d5b4d70c | -13.86608 | -48.50128 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50cb6d20-9b75-3834-b672-567f929e3cf4 | -8.51096 | -48.27863 | 2025-10-29 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be546edb-2682-31e7-ad1a-f00bdb40cb14 | -9.29104 | -47.02134 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a5478b19-aa2d-3438-93df-3d7ffaf1334c | -12.14213 | -45.20908 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1ad2249-12d8-3bcf-bc52-5bda87e40af5 | -14.26833 | -47.32109 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b95f9e4d-d017-366a-be5c-8cb204996007 | -13.23433 | -48.56182 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be01fcd8-2da1-3b28-8fc0-de1dcace0e9e | -13.63507 | -46.48302 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6570c8e-fac3-39d1-9010-2aa6bbdabbec | -15.32477 | -42.99409 | 2025-10-29 03:55:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bf2c5ea5-ba55-359f-afc9-b014daf6dedd | -10.6187 | -42.30376 | 2025-10-29 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a107a6c3-2253-3176-94cd-8bf4012e2339 | -9.80237 | -47.7547 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76b97ea5-a18c-31f9-8abd-b2e335421f2d | -14.52048 | -47.99778 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4725b963-8d38-3810-a80a-8f0d30eb1862 | -12.77282 | -46.6586 | 2025-10-29 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df3bbc1c-437e-331d-8b61-7590fe718226 | -14.06605 | -44.08564 | 2025-10-29 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137d1247-3e56-3b9c-aa40-7a4f84143480 | -14.30895 | -46.52226 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a128ab06-2eb9-3b46-b506-60e7818af064 | -13.47064 | -47.81837 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca8b8cf6-44c2-37d1-8def-80c2ea93c831 | -14.13117 | -41.76709 | 2025-10-29 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31f9b5ec-00bf-30ac-93f6-3bbbb4d85f39 | -13.57382 | -49.60489 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 72b66a17-8ce4-3918-8a79-0da0445c2a86 | -13.23497 | -48.55839 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94daeb10-d6d7-31a5-8f7c-ef8e1d985cc7 | -9.54278 | -46.92424 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7dea70a-1f19-31f9-a869-6b6442a6a829 | -9.49312 | -47.33659 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f021776a-4c23-3311-b69d-4468b3b18302 | -13.24764 | -44.11269 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a054104-9edd-3403-bc6c-af8375e89681 | -11.03116 | -47.84747 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 103e217e-70ee-3651-bb20-0519f775b9de | -13.56904 | -47.33379 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e0905fd-0f23-30f8-83ee-7b0a12ddd652 | -11.59099 | -47.95133 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4754a83-c2e4-3115-a78f-5961962713c3 | -13.42152 | -47.37263 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50c6c306-0434-3c4f-99cd-4ff93d496fc2 | -12.16086 | -47.69405 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6b524fa8-6786-3db4-ac82-cb480185a202 | -13.70177 | -47.67146 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3183173-b5ee-3e6f-baaf-3668c9ff86e2 | -10.51821 | -47.74522 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2497043e-8e30-35d2-8b4c-6a059210fc7b | -8.55059 | -47.01056 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a7c90f8-63af-3e48-b9ec-e4bc93bef1fd | -13.03708 | -46.73624 | 2025-10-29 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e034a5ce-c039-386b-9322-9c38092ed641 | -9.90558 | -44.92783 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c10e41c9-2b2d-3eb7-b915-618e27ba9736 | -12.1895 | -46.71743 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e8033bf4-e82f-3b61-a424-f370eb64166e | -14.19913 | -48.35723 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 309e496f-f08c-3f6f-975c-f89628fed3fb | -9.50432 | -46.9687 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96128e24-f184-341b-a24d-17244c5222e8 | -11.58707 | -47.94438 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6263b8d9-cf47-3dd4-a895-a0abe302c5a3 | -10.22344 | -47.54977 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf5aa3c3-d8a3-3efb-b316-5d60c6183914 | -13.65678 | -46.46425 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f878e872-d097-35b7-a3d1-8ed835c9daea | -13.217 | -47.07053 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b40d839d-b89d-31a2-8dde-3a278abb75ed | -10.62353 | -47.97599 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79269cef-1a84-3138-bbb3-12f8bfb62352 | -13.37418 | -47.41751 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 443e3ff0-aec8-3764-bdcf-1116f797969f | -13.64803 | -46.46236 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27774ff6-5a63-3090-b78d-3fe7c9f3e37c | -10.51932 | -47.73919 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52ef596c-733f-31b1-b347-731460db21be | -14.26132 | -48.11183 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7c143e9a-3853-354d-976d-79d335f72a4f | -14.54373 | -48.00427 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a44f4f4-0d14-30b1-b62b-154c4c3fd900 | -15.8014 | -43.65058 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b83d7d3-e168-3b38-945a-1d6094adf838 | -10.44075 | -44.69939 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9002341-3e00-34a4-931d-61e9993dc712 | -12.64331 | -46.72016 | 2025-10-29 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 267ed649-f22a-31c8-85b3-b05cae7da03f | -11.97716 | -44.03651 | 2025-10-29 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32ceee85-fba6-337d-982f-2124c7bf36ac | -15.20044 | -47.19908 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d44a329-0f80-36d0-84a1-8eccd0da2ece | -11.37336 | -51.37002 | 2025-10-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 519b0199-1b5a-334c-b89a-a9f3ef22b66d | -10.20595 | -45.94628 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8975cfb-668b-3208-a876-37eebe6ac402 | -12.87892 | -48.27621 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83bbdddb-fed9-3a79-a53e-9fef5c12b1f6 | -13.65999 | -48.44222 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e0408e5-d35c-399a-ae95-1532edc78cdf | -12.05043 | -47.81909 | 2025-10-29 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c865a01-6d28-3713-a292-92e543b24b3e | -12.91417 | -45.041 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d1b6e87-518f-3eaf-9994-a31099313db4 | -13.94522 | -48.46563 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b9d78f-1dac-3538-81df-758b55ecf64a | -13.87478 | -48.48293 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8680003e-47b9-3937-8e98-86999d61f1b5 | -9.44377 | -46.89893 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4f8feb24-a5a0-376a-b672-e1e9d5883e4d | -10.85832 | -47.89313 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06590080-3312-3625-8911-168cb27b7ac2 | -12.71665 | -43.89548 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef91cd19-c291-30ae-95ae-fe81f2483d33 | -12.7939 | -44.01027 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8263f4-db8a-336c-82f2-1ef44eddd64b | -10.91936 | -48.0077 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dd85bdd-f29f-3388-a26d-5a25a8e8ee44 | -8.51195 | -48.28107 | 2025-10-29 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a30927-fc0d-3c80-8109-ef73f7444970 | -10.95399 | -47.62344 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac250b07-7943-39d1-9391-701372b7c8f9 | -12.71209 | -46.32108 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f30bbce1-85b6-3029-8e67-ec4024a2e79a | -10.52443 | -47.73989 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17818421-0e36-3291-800b-e69c5d12bbd2 | -9.44475 | -46.89354 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 94c2f562-3258-39bf-815b-8d8092a9e81a | -13.85396 | -41.50628 | 2025-10-29 03:55:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f5ff340-67b2-3b3d-b4c8-861456d3e623 | -15.11497 | -43.26443 | 2025-10-29 03:55:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11905d1a-55af-3c7b-acd8-133528dc239a | -12.9135 | -45.04468 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7adcc5-e955-3154-9abb-80541bfc48d4 | -9.53789 | -46.9234 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97dd3717-2b52-3060-b609-fe0f50339c2c | -13.63716 | -46.52071 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 004e7b31-9276-360b-95da-a14dbece5351 | -9.15586 | -50.13688 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbfc5a09-140b-3200-86fb-753b6e6326a5 | -13.42071 | -47.37703 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
