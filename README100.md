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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf33f113-89cc-3631-98a9-4a5b04e9bb6e | -11.86589 | -48.07498 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20b4c318-9dd4-3698-81e6-2d11f3e5eba3 | -14.36275 | -45.9648 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e3f8950-8f9c-3e5e-be5d-221382f2e67c | -14.44004 | -46.349 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 048f4252-4d7e-3fe1-a424-122c17a66f42 | -14.42863 | -46.35494 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c695bbc2-c087-302c-bafc-22502536dda3 | -13.53196 | -47.27872 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1aa5bdd-da14-32aa-b6bd-6e5fc4a9b4bb | -13.32199 | -47.21638 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2ffcd98-c151-3b85-9c35-8bcadad93ec2 | -13.4712 | -47.23997 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cb9e48c-4d60-37f3-9798-4e9ae497525c | -15.09016 | -47.34615 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c2ae1fd-9ac4-3eaf-928c-e398276ac212 | -14.09014 | -46.65916 | 2025-10-02 04:32:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0ac9c8f-4721-3aae-b2c5-2e5737465b65 | -13.70073 | -48.61472 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19d2fd85-108f-3633-8a48-cad9039b1eff | -13.96198 | -48.11967 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a587c99-e7d7-3b5b-9e86-99b7e40ea38b | -12.7718 | -44.91125 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 049c9e5e-a594-3ab5-be88-cf5043d16a5b | -14.58553 | -48.32524 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2314a245-f913-3d98-b1bb-efc025b00ea4 | -12.03302 | -47.91291 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df2158cd-bf29-3739-9837-eecd599b4dee | -13.78985 | -48.05532 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08720da7-6fee-39f3-84a7-f47f8496eded | -18.5245 | -45.04368 | 2025-10-02 04:32:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3772e32a-84c9-3212-8619-ac2b87b3bbe7 | -14.42534 | -46.10035 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ab12cd7-0832-3a62-94cf-e4a2e46f482a | -13.55869 | -47.28311 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c27ffd9d-ecc3-3243-baa6-9cfcb706d14d | -14.59438 | -48.33405 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd46c0dd-b8a8-3b99-9952-b3be5daa2f3f | -12.93656 | -48.41836 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77f16b9b-3c8e-3710-8531-0fa5ab557983 | -13.08206 | -47.07133 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a2d965e-2de5-3c41-9496-5a26e2d9ab17 | -13.21699 | -48.44666 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8987990d-17b9-33d5-a0d4-75afdb989099 | -13.08374 | -47.08261 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 707d82ee-c030-3151-8657-e51f9dbba61a | -15.27917 | -46.40176 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c827c76f-1b10-345d-9b0b-098b4d2ec58e | -11.86199 | -48.07798 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504d15e6-d2d1-3a3c-8fc3-8c3661287b4e | -14.43149 | -46.35928 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c4880ac-d9c9-31cf-815d-7c4577718983 | -14.30956 | -45.98827 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cd627f1-20cc-3580-94ad-6da33ef9dd54 | -14.40346 | -46.08106 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d45b838-0fa0-3114-9c24-c8859851df2d | -13.34047 | -47.33995 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d5475a4-1bfe-386b-a291-3c98790a7e17 | -14.88091 | -48.12843 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3741ade-fe23-3f52-ab97-91a1a61f9834 | -14.4878 | -48.45149 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d78639b-8cbb-324c-a109-8d33cffef969 | -16.57966 | -45.1157 | 2025-10-02 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d621fcc-9d48-31d6-965b-977dcef0827e | -12.20795 | -47.79248 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 320be8f7-5b35-3313-ab99-139da1f77a1f | -12.70175 | -48.57434 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bb7f36d-d220-3131-b15f-5772b8c3c924 | -15.30052 | -46.39262 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e562c2b-2259-3d94-8c93-97c87bcb961d | -19.51537 | -43.61573 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2233cd62-1e87-3492-afe4-560c44be416a | -13.46843 | -47.23576 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e6b1c09-2538-3c45-849b-80d45bafd507 | -15.31877 | -46.29295 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6e52dda-4b53-3fb3-93ff-fefe65466d4a | -13.35987 | -48.12326 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1784495b-3879-39fe-b476-99013d87519c | -14.98663 | -46.90914 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35b7c8d4-1e2e-3cac-8cc6-7e6b45a91cdf | -14.34322 | -47.12719 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f59ea07d-3848-3920-9147-f1bccd148581 | -13.80143 | -47.5308 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 646a789a-ec14-3462-bbb9-d6b7acf867f8 | -12.6592 | -46.87536 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f586f2-f55b-3ea1-8b82-e673801d3ebc | -13.8623 | -51.25011 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a7ce089-1419-31cf-8127-0961fde08fe1 | -15.77588 | -50.15976 | 2025-10-02 04:32:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d1864f6-ac75-3117-beb1-e48f36c73db1 | -14.88151 | -48.3334 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26ffef6d-4d8f-3950-8fd6-7e72b75b828c | -12.94153 | -48.43013 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cabf2863-e7ee-38bf-9566-80295f37edec | -14.90317 | -48.32602 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1b6ed76-7f5f-3a17-9ec4-570056c4e7b7 | -13.47455 | -47.24051 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b8cb734-90b1-316a-844a-f6d93dee528a | -14.34266 | -47.13085 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a18411d9-c84d-3454-9d5b-f0ea6319030d | -15.26677 | -49.30656 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43800b74-a949-3e0c-b79c-6c32d423413e | -12.25698 | -47.82281 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9883e8c-e508-3ca9-85be-2c811b065741 | -12.01736 | -46.63073 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 679bade2-96e4-3f9b-805c-6188e82a90fe | -16.09537 | -51.04773 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f756e77d-a987-3fe3-947f-be7a582cd14f | -13.36591 | -46.33501 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f718cb0a-2f22-3f77-81c9-31243583eff4 | -14.70231 | -48.20514 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32d2a3b1-7d77-3a7d-89bf-d22f65a4b241 | -18.50808 | -44.04324 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16c9e089-e0a9-3e2f-9d11-ab037e768b15 | -16.29075 | -45.24501 | 2025-10-02 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a845189a-347c-32a0-a12b-03e19b2e8d2f | -12.87155 | -47.01171 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6baa64a3-c5c2-35cd-9202-ebd1ef41ab61 | -15.19884 | -48.16979 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c600d104-0c64-3670-b5ac-0894433282e8 | -13.2209 | -48.44366 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 038a6ba4-856e-3398-a658-a9dd9c519dae | -13.35383 | -48.09674 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e8dfce-431d-3308-8dc3-c06205f8b300 | -12.94894 | -46.37307 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55ef05ac-4a84-35b1-a3f8-e04c436ee221 | -13.4248 | -47.79887 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9d93402b-a24c-3f77-a188-937ca44954f2 | -14.90425 | -47.21585 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae323c57-dd5d-358c-a20f-5e562a5b3a8e | -14.35336 | -43.84521 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 437c7dd8-3785-3a36-94bd-0aa9f24af4e6 | -18.19815 | -43.57194 | 2025-10-02 04:32:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10770b9c-ed91-3ecc-ae99-306f5914eb34 | -11.85379 | -48.02205 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5871fd0-7964-31f5-81f9-8934c4dbfbad | -12.94332 | -46.43282 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f70d311-a0a1-3896-a15d-fbf1a3dae0bc | -16.36423 | -47.08234 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b956feb2-2b31-3e8a-9480-9af594c9a958 | -14.42187 | -46.09986 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9f07379-1996-3671-8b83-d3613c6a09fe | -13.94974 | -48.13227 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 18a2cdef-57ff-3d83-8d77-c27976a5afe2 | -15.39599 | -47.05998 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4f0a7e1-8414-3fca-9b91-da54fe72c0b8 | -14.49453 | -48.43062 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63cb7f51-2e31-3dcf-b207-888fa709c881 | -13.31236 | -47.82433 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b1f1aa-3f07-3461-83b2-8e7453c288a8 | -15.28908 | -46.39849 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dc4281b-9b22-35d5-8ea2-6b4c6de33d4c | -14.30492 | -45.97173 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4cb8aa4-b47a-398e-9003-347279f5ba4b | -18.3457 | -44.50706 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a32914ae-91ec-3ccb-88c5-36525022e4a4 | -12.81583 | -47.03937 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21b1f4fa-9f1b-3f3b-b785-4df4ca3c91a4 | -17.07652 | -44.91164 | 2025-10-02 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60e2f709-c2ed-33f3-a0d9-f04ec71ae05c | -15.39348 | -44.97228 | 2025-10-02 04:32:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab592193-f61b-3fb4-b768-f49d2367ea32 | -15.6018 | -46.917 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a158569-f66c-3995-8aa4-a4d32a1470a2 | -14.32748 | -45.98704 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50d67c43-f768-35de-87bb-2aac4a39cfed | -14.59319 | -46.7215 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c620b584-42f6-3c10-9b28-e8c92ad23715 | -12.84469 | -46.94138 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88ff87eb-01a2-3ea0-ad7b-e7aa5a9e88f1 | -15.22637 | -50.10432 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e408e5f-daa0-328a-8644-00c283319e40 | -14.69123 | -49.61683 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c90433d1-6afe-3faa-a2eb-6a8c68c73e8d | -19.71502 | -45.91155 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f450b1ee-bafa-3482-aac3-57833ee57100 | -16.03826 | -50.91366 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06270a01-703b-3177-9d15-207571b4f2ff | -11.91568 | -47.88299 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c0348a4-8bb6-376a-ad30-262ce7bfa544 | -12.84249 | -46.95558 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90cfe7fb-98ba-3abe-bffe-134c9b2cd736 | -19.01923 | -49.75193 | 2025-10-02 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb058a2c-4eb4-393d-816a-a6058f32721c | -13.15334 | -47.84517 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5f11835-edbb-3475-972f-4d8e596bbf3f | -12.66622 | -48.57195 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7446ecd8-623e-31c8-97ac-8313485bace6 | -15.30396 | -46.39322 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d76cecf5-92e3-34e1-8067-c7a9b02bd84a | -15.22775 | -48.73675 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f4b8159-a2eb-388a-9252-bc391fbf8d9d | -12.20462 | -47.79193 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 040ddbea-619e-305a-95e7-a8f1ba9189fb | -13.42147 | -47.79832 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b676834c-0710-3eaf-8ffb-9e0eb62d9bac | -14.41036 | -46.10593 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a235a7f5-f8be-3d3c-af78-2940c185e4ba | -12.84134 | -46.9408 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README101.md)
