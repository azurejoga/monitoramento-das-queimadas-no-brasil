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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f14b6886-3518-3d60-be16-6ded87328143 | -21.62306 | -41.21072 | 2026-07-16 04:23:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5bbd3f55-e308-3ddc-93c8-d4706749240e | -21.90095 | -47.161 | 2026-07-16 04:23:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21068f1b-4f66-36ef-b686-0966e09a2f8b | -17.59718 | -44.60281 | 2026-07-16 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb6e0521-80f4-34b7-af7e-da3301376118 | -20.33865 | -46.61922 | 2026-07-16 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91cee471-8fd7-3c6b-90b7-390656a8eb66 | -20.62898 | -46.28682 | 2026-07-16 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d17ac02-697d-39b5-8c97-faec6f0e6ebe | -21.52523 | -41.23149 | 2026-07-16 04:23:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a864ee47-6cf2-3481-a519-3fe08ebfdbe6 | -21.65446 | -44.18176 | 2026-07-16 04:23:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 406b92f7-124c-3a44-ac6a-750bfd0e7e0d | -16.4504 | -51.06578 | 2026-07-16 04:23:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e6f154f-d747-37d2-b811-2f25f8776355 | -17.91006 | -44.4083 | 2026-07-16 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b1b0fe4-1e33-3f96-aca0-cd9ca1eaf60a | -20.47983 | -54.98315 | 2026-07-16 04:23:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5a5c8c9-e75a-3119-ae8c-42fbeeb7f247 | -17.70257 | -42.66389 | 2026-07-16 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fd2417d9-eabb-32a0-8208-125efcd42134 | -18.98798 | -39.97048 | 2026-07-16 04:23:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 015d80bd-9cbd-333f-a604-f9208c3d82a0 | -21.40841 | -43.88072 | 2026-07-16 04:23:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0374c5d-dbfc-37b2-8b70-0607cdb6f33a | -22.27786 | -42.88824 | 2026-07-16 04:23:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e58f6ef9-30d9-3570-b76f-85787fd28fea | -18.99755 | -47.89753 | 2026-07-16 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b7480de-90de-310c-9c26-b90d4707838a | -18.27624 | -43.69683 | 2026-07-16 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661b366c-3b84-32bf-b59f-f7d40b1b6221 | -19.83902 | -45.40691 | 2026-07-16 04:23:00 | NOAA-21 | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdaad23a-dd23-3b9a-a7a8-29d5252fde79 | -20.534 | -50.55395 | 2026-07-16 04:23:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 151369b4-510e-3122-96aa-2711a4ec5dc0 | -19.28303 | -43.70065 | 2026-07-16 04:23:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e77ccc6-b1ea-39c6-a663-0f410715496e | -20.5204 | -54.70205 | 2026-07-16 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e492d34e-fc5d-3c19-8aec-6f2eb6c8cde2 | -19.30675 | -47.44298 | 2026-07-16 04:23:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08cc795f-24a2-3b60-9719-bfac1f30960c | -19.28441 | -43.70258 | 2026-07-16 04:23:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d94f005-c156-3ca2-b67a-02c07c7a7d5c | -19.92904 | -53.58693 | 2026-07-16 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7b851f6-e0d5-373a-8302-93a426592fc3 | -20.51895 | -48.85603 | 2026-07-16 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44fcd393-8a5b-32ad-a1f2-b7c2e4ed1eba | -17.84427 | -52.48804 | 2026-07-16 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdb1c1cd-acc3-3f06-b62e-426e118721d4 | -21.35489 | -51.04459 | 2026-07-16 04:23:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c24c4c19-6d52-3602-bb02-f096d9fee97e | -18.62386 | -54.91576 | 2026-07-16 04:23:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cb2ef958-e1b0-3cae-a626-a7f34e9bf169 | -17.70325 | -42.65887 | 2026-07-16 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1152fde4-cbda-33c1-93df-61443f9f75ff | -17.59366 | -44.60239 | 2026-07-16 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f3b08c-9968-303e-848d-bfac9490fa0d | -21.52472 | -41.23622 | 2026-07-16 04:23:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 624e2d29-0b1f-3878-9530-0e6204f4464b | -20.51835 | -48.85975 | 2026-07-16 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2bdf3910-e6f2-3ad1-9ad1-821b48b0cc2b | -19.83335 | -57.95422 | 2026-07-16 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1fd5ebb3-8c70-3b6f-b07c-05ae66fcfb7d | -21.82225 | -41.41048 | 2026-07-16 04:23:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c91ba1fe-a9a8-3c60-9cae-9291eae6bf03 | -19.01364 | -45.74912 | 2026-07-16 04:23:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b7d6f9e-06d7-3878-8d6d-6221b04b0c93 | -21.67031 | -56.32029 | 2026-07-16 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee80dd81-1a6f-3ac2-9039-582451b4eaee | -22.37628 | -49.79226 | 2026-07-16 04:25:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42ca41b3-adff-3efc-8424-aabe03790a75 | -23.56182 | -47.51645 | 2026-07-16 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 9ed55b73-dbe8-3bb7-b985-574cb528cda1 | -22.37691 | -49.7884 | 2026-07-16 04:25:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c58ebaef-fa1c-3992-b3f9-813cd8c04bb3 | -22.78842 | -49.35162 | 2026-07-16 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 356ee29f-ebd4-3cd3-ae12-4b9ecc99c3e4 | -22.7514 | -51.94554 | 2026-07-16 04:25:00 | NOAA-21 | ITAGUAJÉ | PARANÁ | Brasil | 4110904 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 679fefb7-ea15-3995-a83f-11cb4c3ce50e | -22.78903 | -49.34785 | 2026-07-16 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19a2a8d1-f2ba-3c52-982b-c3fe4b82fb60 | -22.37964 | -49.79289 | 2026-07-16 04:25:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 364eed39-e7c6-3e05-870c-bfe75495b0d7 | -22.7522 | -51.94104 | 2026-07-16 04:25:00 | NOAA-21 | ITAGUAJÉ | PARANÁ | Brasil | 4110904 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| c2f6f4dd-1a7d-370d-83e9-ff82b3c44602 | -22.96904 | -52.70951 | 2026-07-16 04:25:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 977ec0b7-36d5-3965-a750-502575850958 | -23.34201 | -52.33092 | 2026-07-16 04:25:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d429e9b6-135d-3fa7-b32a-92ecc6f3ccb0 | -21.66676 | -56.31358 | 2026-07-16 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b95caa68-4ae0-3461-8143-96127d21da60 | -23.33838 | -52.33013 | 2026-07-16 04:25:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8d2d0553-5ec8-3ff2-81ff-ac29edb05297 | -21.66563 | -56.31904 | 2026-07-16 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ee0fda1-e322-3206-ad27-a2d432a650ff | -22.38425 | -49.78584 | 2026-07-16 04:25:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4cea8aab-6f92-3f9d-adb8-66b990f2d687 | -23.14529 | -48.66806 | 2026-07-16 04:25:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12f92e9e-e678-3867-b417-17ad9a6f8be3 | -22.9699 | -52.70475 | 2026-07-16 04:25:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6bb7745c-3a5d-3281-accc-45c8ac31178d | -23.33754 | -52.3348 | 2026-07-16 04:25:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2b577caa-9d8c-36c2-aaad-cac008fc5893 | -23.56516 | -47.51704 | 2026-07-16 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29198147-5556-3fed-b821-3da3821ea842 | -22.3809 | -49.78521 | 2026-07-16 04:25:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7542706-eca7-37ae-887d-04905dc57b75 | -21.67145 | -56.31482 | 2026-07-16 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b10f90-95b1-3576-9c36-d3d454ea1a76 | -23.14199 | -48.66745 | 2026-07-16 04:25:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 193cf110-79b4-3e9d-8ce4-f71833e3f261 | -21.9853 | -54.62755 | 2026-07-16 04:25:00 | NOAA-21 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43e88f07-0878-3615-959e-9ad73028e8fc | -29.87149 | -54.70359 | 2026-07-16 04:27:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 4132d558-8b2f-36bd-9f2b-b8f81c563da5 | -29.2076 | -55.65146 | 2026-07-16 04:27:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| bdbed1b0-ce27-38ca-aed7-db1accd8ba32 | -29.20567 | -55.65341 | 2026-07-16 04:27:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 49bb60e8-d29d-3713-a96b-2e6f4f6f257f | -3.96796 | -47.20641 | 2026-07-16 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb88a423-ad9f-3a86-9593-4707a98f343d | -3.73762 | -53.73446 | 2026-07-16 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c01c052-9a78-3517-b015-d4f1e6c306b3 | -1.81637 | -54.47763 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b89d9d57-bea9-3cb8-ad5a-6b8f73655f37 | -1.63889 | -54.46981 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2663a63d-ebdb-3869-8bc4-b6db4ab26063 | -1.64288 | -54.46667 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b141475a-a5c0-3857-b849-e8a965dde86e | -1.63605 | -54.46556 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a23b45fe-1e03-370f-b635-067cd2ec87e5 | -1.48695 | -55.28326 | 2026-07-16 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc650bcd-c53e-303f-8ce6-a36a5a4070af | -1.48361 | -55.28273 | 2026-07-16 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fbff34d-7088-373f-89af-a862d25c771a | -1.63947 | -54.46611 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ed3ee31-6ed5-3204-8f8a-c1278e05c7ab | -2.79487 | -49.52624 | 2026-07-16 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c100c5c3-9b27-3968-ac46-f0c00766e9a3 | -1.82323 | -54.47868 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e909a967-d47a-3806-8127-420abcb961df | -1.6383 | -54.47352 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85b29d51-06c4-32a6-b0dc-416eeacf457a | -2.79021 | -49.52555 | 2026-07-16 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3238bc7a-bccb-383e-9808-3670c5969fb4 | -1.64347 | -54.46292 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0387b8c5-246d-377d-a7ca-f625c5686d9d | -0.08949 | -51.28205 | 2026-07-16 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31de244e-43dd-30e4-87a5-993ee461004a | -2.79273 | -49.52666 | 2026-07-16 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e68740f9-9007-3943-ae8a-2351ab5a2c95 | -1.4875 | -55.27974 | 2026-07-16 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ff152ed-2377-34e4-a044-a06a2bd0019d | -0.09003 | -51.27862 | 2026-07-16 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83f25cf3-36fd-396e-a3f2-c1065e732f5b | -1.64005 | -54.46239 | 2026-07-16 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c20a993f-c826-3941-8e16-0765078f0095 | -12.45038 | -49.5867 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59d78bcc-4472-38a1-b978-ca16bd9ce9a2 | -13.26367 | -45.14723 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 24be9199-d362-37bc-a056-a638cf94b266 | -13.2665 | -45.15016 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 42ac1b8e-acdc-3a4b-94bc-2fd0a335e6dc | -13.54978 | -47.80718 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a968c8b9-dc71-3bf3-bd3e-fa363da426c1 | -7.89981 | -47.69698 | 2026-07-16 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836cb5a3-73af-3faa-8ae8-a4ecc80d17e5 | -12.44291 | -49.57864 | 2026-07-16 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d012e6c5-b935-3028-b4d2-80be9837f764 | -13.5526 | -47.78233 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25a3aa1-f92e-37e1-97ff-0d563d570439 | -6.12589 | -55.81004 | 2026-07-16 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7bec663-6a28-30ab-b6c7-69057432c0e7 | -13.26506 | -45.1336 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 10adeadb-e281-385f-92c7-657e108b3762 | -11.78973 | -47.09355 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2c5384f1-37a5-31f6-ad24-5adf815d23a0 | -13.25868 | -45.1255 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| bcc2239f-e5db-3d0b-8f87-efc75926541d | -13.43384 | -49.13397 | 2026-07-16 05:16:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8eda0623-7214-3401-9004-f223f9870ed9 | -13.43428 | -49.13009 | 2026-07-16 05:16:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2a0569af-939f-336d-877e-4c31426d8c49 | -9.08541 | -59.49693 | 2026-07-16 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39304e00-798e-3e54-b197-91bf6eebad32 | -13.26296 | -45.15425 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 580b1680-2c25-3fe2-b9f0-421e2442f632 | -12.07438 | -49.915 | 2026-07-16 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b794d9b0-7480-3bfd-9384-4dc55921281b | -13.25796 | -45.13258 | 2026-07-16 05:16:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 660097b4-85f6-3d8d-9a27-cc7ac66166ca | -8.92045 | -64.30266 | 2026-07-16 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a72722d1-ed1b-3f8c-b454-5e2d8118e04c | -13.52646 | -47.79476 | 2026-07-16 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59ef2be3-ac48-3976-91c5-9b0731b64587 | -7.8936 | -47.70002 | 2026-07-16 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03ae295b-2f9a-33a3-a17b-c1106b8efe62 | -11.79107 | -47.09585 | 2026-07-16 05:16:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README5.md)
