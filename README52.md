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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15c24d66-2db2-37b3-842f-862b6787747d | -19.04656 | -48.13752 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c040fc2-27da-3c79-be4d-ae7b243afa87 | -14.09154 | -46.65997 | 2025-10-02 04:04:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 61a992ae-a1b6-395c-aa85-b78ad9d61f50 | -12.69834 | -48.57891 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f155ef7c-2c6e-36cf-97e4-e8d42236e30c | -13.29887 | -47.19962 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b48dcff9-f94d-3c1f-a49b-e72d3c127591 | -14.69886 | -49.61529 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a55217-6e24-3ef3-ad6d-2a0d7018ac31 | -17.39556 | -47.16623 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 275b0dc8-60e8-3978-8223-4c3aee4ac668 | -14.47457 | -48.43505 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7dba4a31-6661-3462-973b-aa09a48805e8 | -13.76385 | -47.97727 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce560048-89a3-3c57-a3b6-56bad14c426e | -14.90579 | -48.33582 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 321e1299-bfc9-3c37-ba16-6eba5fd664e6 | -14.48953 | -48.42801 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 207270f5-56ec-3642-8f21-ff617d046a67 | -15.15515 | -48.39299 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe23cbdb-ee3d-3da7-897c-f122ce944564 | -13.16144 | -47.81781 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2bb04a5d-eda4-3c5c-8bf3-8ca29b61a025 | -13.30792 | -47.5818 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00368cfd-3dc7-3910-8c5a-517d512a378a | -14.90808 | -48.32331 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2c210c7-c169-3206-9355-ddc351b13810 | -19.4925 | -43.60688 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fe5657a-fb1f-31be-831a-5a3d008e9959 | -15.36423 | -47.0694 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a038cbe7-6194-3032-9462-d5f9ac5990c9 | -14.30781 | -45.98281 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c0dec7f-9954-35fa-9797-b632c10b986e | -15.27478 | -46.39719 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22051b08-88f7-34d0-bc02-03dde620b4f0 | -15.14121 | -48.02411 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ffd150d-e230-3900-8468-1ae4741be9fc | -15.29181 | -46.39004 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f0b55ac-316c-39c2-b121-575582da89d0 | -14.70202 | -48.20939 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16ee3774-2dde-3d6e-b3c2-e44618d1ce48 | -14.65252 | -48.2599 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f06628c-1faf-3e17-8f7e-e14ebd230511 | -14.86543 | -48.28791 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a921efd4-36f5-3920-9d6b-4717a15d4ade | -14.57833 | -48.31472 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3a5bd8c-7486-33b3-b9b6-fb99bdbb8c07 | -13.08742 | -47.07751 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ae78c7-d427-3651-a063-f2a890a364fc | -13.08061 | -47.09221 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc687ca8-94ee-37c4-b0bd-bf58a7f7cbef | -14.22462 | -44.9303 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7628684d-913c-3b99-9a54-7b0fb6bbea37 | -19.72208 | -45.8935 | 2025-10-02 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f17852a-031a-31ff-9219-324c052ff128 | -15.79332 | -43.73618 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1b32039-c9e1-3dd8-9ed2-038e82a9bcce | -13.74501 | -48.7022 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 988299c4-31fd-34aa-aac5-64374dbe5f98 | -14.9131 | -47.23004 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9061f9ce-2c98-3599-a503-961008eca631 | -12.94604 | -48.43771 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a215512b-1d7f-34e6-b7e5-cb0e326b2b2c | -14.47062 | -48.4319 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 844f6773-2712-36fa-867a-8d055f1f327a | -19.76955 | -46.58226 | 2025-10-02 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fdd7473-b0d9-3f3c-b09c-76608f6a8121 | -19.51951 | -43.60796 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74f5ca2d-77e3-3b96-a4a6-b19e19d2fa37 | -20.73516 | -46.03561 | 2025-10-02 04:04:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e958b9b4-80a8-3374-8c1c-de5ce12189ff | -15.3243 | -46.29575 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d94610-e718-3e0e-b31a-c5c5e7a321d3 | -13.78261 | -48.05432 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5dd80220-c37a-3e25-8fde-72961e68ec22 | -13.75319 | -48.01149 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a49bd439-2e31-3908-9190-bc70055d9ee3 | -15.29979 | -45.08004 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d89ad7-d268-39d6-a819-3bcdb56506fc | -14.36503 | -45.94419 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61971c00-0e5b-39e1-9813-7551d23558ca | -19.57922 | -41.90511 | 2025-10-02 04:04:00 | NOAA-21 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f53c862b-97fe-3360-bbb0-cba9530a2f1a | -13.52612 | -47.26663 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24a0c313-82c6-3e93-8165-61d80035e295 | -12.70197 | -48.58503 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e0efd2ce-00f0-3cf3-a2f1-6cae740d0fa9 | -15.2839 | -46.39577 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4694b64-e6e5-3aea-9012-8b9a733deee6 | -12.69349 | -48.55353 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b51126e5-ef7a-336a-92ad-48129f1d3b25 | -14.7214 | -41.06788 | 2025-10-02 04:04:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e62fa347-8590-3e5d-9017-504a2a2eab9b | -13.40009 | -47.77521 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 154481a8-68c4-38e4-bd44-5631128dcd98 | -15.20126 | -48.17054 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 621cdc0c-4f76-34f1-ad4e-bebbd6945053 | -15.08814 | -47.34997 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e025235d-7100-3051-be68-d97e53197572 | -13.61831 | -47.28909 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd17f25-7ce7-33e6-ba6c-58b103958fcf | -19.90599 | -44.69061 | 2025-10-02 04:04:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d024cffc-4def-3985-8116-191a84ad37ea | -13.38655 | -46.94701 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5b7ffe5-ce3d-3aa9-83db-95e0aef92ec4 | -14.88807 | -48.31047 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 750c2a0e-763d-34b3-b242-030db01c30d5 | -13.69139 | -48.63848 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78e60c63-fe37-344e-9c32-1199e33bad8f | -13.64449 | -47.1916 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4189bf45-af6b-3ebe-ac23-85840986e809 | -16.04922 | -45.72498 | 2025-10-02 04:04:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9502f213-ac5a-3266-b3a3-73a8bbbdc5b6 | -20.1349 | -46.34734 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8ed4cc4-1584-3702-9cbf-3e44b109d9ec | -14.40416 | -46.07737 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e4aebc2-e5ef-386d-99e2-bd9a2253fe46 | -13.41956 | -47.80415 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 467cf3b1-b786-3137-a3b1-f94a6084e3e9 | -14.41943 | -46.12453 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9095422b-4dce-382a-985d-b4e47dfbcda1 | -18.58868 | -43.03939 | 2025-10-02 04:04:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0f9164b-f873-310c-9ecd-fb0b796ddd02 | -13.8007 | -47.53266 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 978a90f4-eec2-3ba2-8e8b-7b6fc833c8cc | -17.40039 | -47.16153 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e450faa4-42c5-3e83-8813-66d476ff1e0b | -15.74402 | -43.6779 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d1b9263-60a9-3667-befd-01feb95eefa8 | -12.4193 | -54.35402 | 2025-10-02 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a8a902b-9a70-3e51-bd22-b54c77f05425 | -13.17749 | -47.83825 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31c08a85-ebd8-3bba-8af5-2bc233f44d1f | -19.26137 | -47.35015 | 2025-10-02 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46ccb72a-e859-3436-a8e0-810be680dcc2 | -13.19554 | -47.83713 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 511992da-9d6c-324e-b4fd-b432edbd359f | -13.32784 | -47.80732 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3decbc11-9c99-33ce-b51d-587d2eeee784 | -16.0428 | -50.87793 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d44d4ac-5480-3d5c-ae20-135a60b04594 | -15.84514 | -46.23959 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10ee34de-f1f4-3c2f-86c7-81127789c447 | -19.27227 | -43.21337 | 2025-10-02 04:04:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 730115f3-580b-3a05-bfdd-ffa4fec66b18 | -18.50287 | -44.04287 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a94e045-91f2-3494-adc9-33953075f266 | -17.32647 | -49.38759 | 2025-10-02 04:04:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7710e70e-3cc5-32a6-982c-b2de82bd4b1e | -14.41178 | -46.07851 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 506a5b6d-17ce-3851-a6e5-83cd7cc1cc9f | -15.28068 | -49.30444 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51d1d384-33aa-392c-afac-d4511c043168 | -15.09286 | -47.34695 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2545d986-5cee-3b0e-9c07-e7975b62a15b | -12.49776 | -50.24414 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b55fce50-0ff3-30e2-80a1-cbeddeff7375 | -13.42532 | -47.7969 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 23cfd8d1-1eae-3abd-b3b5-30cd13b8ec1d | -14.90109 | -48.3126 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dcc1e54-e32e-3a8d-89d3-dde789c425df | -13.21578 | -48.49372 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d8ddd70e-192f-34bd-91cc-0c05d709cf99 | -12.57187 | -49.89074 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d66565bc-b7ac-32fd-8a83-3977b84c35e8 | -15.29566 | -46.3905 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3875d2a6-d0f1-3ec0-8d4e-108e9ff287ef | -19.6286 | -44.90131 | 2025-10-02 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ee6b816d-9e0e-33b6-8f15-674c011dbb34 | -13.31098 | -47.82661 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfe76beb-9943-3be3-9a12-ab02c617db69 | -15.31586 | -46.29922 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee310d2b-f8d6-3820-9fce-4f40accaf477 | -13.77515 | -48.03847 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa836647-5b4d-32a2-b8f3-34a37da18af2 | -14.47902 | -48.43555 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b952c706-08a8-38aa-994e-71f1e87073c8 | -13.67565 | -48.09155 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54daeb44-85b0-3c2e-8edc-f6ce10f79c96 | -15.32439 | -46.40588 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c68e9fd7-8cd8-3d2f-9db4-c12273bf45d0 | -14.31747 | -45.99443 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e4d36bc0-1d5e-392b-a2c4-5410d3057bef | -15.3033 | -46.39178 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b265bd1-2776-3427-b4eb-66f9d95e80e1 | -19.26223 | -47.34797 | 2025-10-02 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee1426b4-3c0b-3192-8a58-d971eaf5c5b3 | -16.04336 | -50.87513 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd613a09-81db-3e47-9af0-6af02b85c1de | -20.49251 | -43.93108 | 2025-10-02 04:04:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2c8d266-9a85-3852-bf13-e96b82802eff | -12.94401 | -48.43222 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f09f3c6b-c604-3b11-8d5a-8ef360a3106f | -15.33482 | -46.25838 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1678b59-359a-3590-94f7-a4995d1cc809 | -19.67724 | -43.87709 | 2025-10-02 04:04:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08b60a7f-c329-3eec-8869-a70d3e970ee5 | -12.94725 | -46.94202 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README53.md)
