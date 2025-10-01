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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b6e687-195d-3ec9-a363-f824823e4c99 | -12.4622 | -50.2284 | 2025-10-01 11:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 190.1 |
| a00750e2-6b49-3af9-a517-157149bd5bbd | -14.3714 | -45.9172 | 2025-10-01 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| accbb35d-6383-389a-ba2a-02630a188473 | -14.8026 | -45.7713 | 2025-10-01 11:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 5ba5b9b9-c9d6-3c03-ab69-0516975cb2e7 | -14.3514 | -45.9437 | 2025-10-01 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 73fdb74f-2d28-33be-834d-ab971f95f56f | -14.3519 | -45.9206 | 2025-10-01 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 985885d8-177b-362a-ab35-088fb10ca01e | -14.4943 | -48.4553 | 2025-10-01 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 12301a46-cfd9-34c9-96f0-378ea8b8e27b | -14.8016 | -45.8178 | 2025-10-01 11:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 107c6af9-d983-3c38-9ed3-5440724334b7 | -10.9769 | -46.5443 | 2025-10-01 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 911e8508-b7dd-33d3-ab60-6304e558bc87 | -10.8421 | -46.6514 | 2025-10-01 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| abd92088-f5a6-3a46-8f52-dfa54abf7faf | -11.8482 | -48.0595 | 2025-10-01 11:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 5e699e37-c275-3d97-b638-b4cf1c673614 | -8.5404 | -44.6975 | 2025-10-01 11:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 22394b79-eda8-3463-bcac-2073114f565c | -11.9411 | -47.0675 | 2025-10-01 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3da1d4c3-2a5e-3c61-b739-e9e2a67ab4cb | -14.3519 | -45.9206 | 2025-10-01 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a977df1f-31ab-35ce-8a97-92820b01c41b | -14.3514 | -45.9437 | 2025-10-01 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| eed0d8bf-73a8-3474-82aa-40f93dd1701b | -12.4622 | -50.2284 | 2025-10-01 11:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 0f256a7d-6e3a-39ec-8575-532bcb8508fd | -14.3714 | -45.9172 | 2025-10-01 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4b2791b1-3e32-347f-ac54-daa24e6c4ce4 | -10.8417 | -46.6739 | 2025-10-01 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 16236bc1-3dfe-3375-84f4-94018a46fd0d | -8.5404 | -44.6975 | 2025-10-01 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f116f59a-a152-3087-bdac-ce47f503cac4 | -10.9769 | -46.5443 | 2025-10-01 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 67e90051-9b70-34a1-be07-b9e4f16b8b11 | -14.3714 | -45.9172 | 2025-10-01 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9e4c3135-b48e-3058-9e23-3ee94cc8efcf | -10.8234 | -46.6313 | 2025-10-01 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f8e4347c-f212-35e9-9b55-b6cda72b5778 | -14.3514 | -45.9437 | 2025-10-01 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 27da6fe4-18ce-3b7d-9565-d74418e0983e | -10.9773 | -46.5217 | 2025-10-01 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f92dd636-3eba-35a2-aa80-e50b145d0110 | -10.8421 | -46.6514 | 2025-10-01 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 19bfc60c-a16b-3489-8b6b-90091a55ef0d | -14.3519 | -45.9206 | 2025-10-01 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d3f31d69-2bc8-33c6-abec-0b90b9fb410b | -11.8482 | -48.0595 | 2025-10-01 11:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| bb16d8b3-e56a-30ac-b41c-45c9a701d744 | -10.823 | -46.6538 | 2025-10-01 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 34b1d262-db4e-35d2-9f5c-d317546e0aa1 | -14.3519 | -45.9206 | 2025-10-01 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 58624dec-9dd1-36c8-8f29-2d4ca3f39b98 | -10.9579 | -46.5467 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ac36e1e9-aa79-3d49-8191-233d1a030544 | -10.9773 | -46.5217 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| dea27cdb-ada3-3354-ba0f-3a9f3e400d58 | -14.9733 | -46.8896 | 2025-10-01 11:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 468cde32-432c-3963-ab73-f111814a9fb4 | -8.5404 | -44.6975 | 2025-10-01 11:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4056d3ec-cba1-3b49-81aa-38dccd2411ec | -12.7022 | -45.2715 | 2025-10-01 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| bbe0ede0-a242-3f7c-8ed4-fa1487f7162a | -14.3714 | -45.9172 | 2025-10-01 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 5eb4f308-6abe-39de-a4a1-39a15b08f3aa | -10.8417 | -46.6739 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cdba847c-bc11-30ec-a7c0-fa2911f08315 | -8.483 | -47.7983 | 2025-10-01 11:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| fb82e15f-1710-374d-9147-340481a46b00 | -14.8016 | -45.8178 | 2025-10-01 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 6eefaa12-b8d5-3049-b0c9-d283cf192045 | -14.8021 | -45.7946 | 2025-10-01 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1373f796-328a-3b86-94f4-dfac838fce16 | -11.8482 | -48.0595 | 2025-10-01 11:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| b877ad36-0c8c-32b8-90a1-c7fa082f84de | -10.8421 | -46.6514 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 22250025-5850-31b6-a4d4-435e598d39c8 | -14.3514 | -45.9437 | 2025-10-01 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ffe80fdd-7c06-331d-9354-7cdb327e5134 | -10.823 | -46.6538 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 0258eddb-cb27-3ea5-89a8-d0edf3ffcb48 | -10.9388 | -46.5492 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 738fe95d-dd77-3bba-8e74-6ca7148e15ed | -11.9411 | -47.0675 | 2025-10-01 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 292d4e3a-c64b-3d2d-97b0-01f5db60a8e8 | -14.1926 | -46.1091 | 2025-10-01 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 531cabb4-2193-3fe9-9f13-97958cfa20dc | -12.1368 | -42.6547 | 2025-10-01 11:40:00 | GOES-19 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 756fb76f-9f1e-306c-8c9c-92cceaf833b7 | -11.829 | -48.0619 | 2025-10-01 11:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 42add47c-937e-372e-813c-ee5399e7d0be | -10.8234 | -46.6313 | 2025-10-01 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e4ab750f-9294-38a3-ae65-0176c8619ef1 | -14.4943 | -48.4553 | 2025-10-01 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9f015e81-3988-3af7-a8be-114741b36401 | -11.8438 | -44.964 | 2025-10-01 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 663143dc-9d5c-3ec5-93e6-613b0b237fea | -14.3514 | -45.9437 | 2025-10-01 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7e21b33b-ac59-393b-b4b8-dbaaef24371a | -11.825 | -44.9437 | 2025-10-01 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 2215f698-4d7d-3d24-8bc7-d7837e635acd | -12.7022 | -45.2715 | 2025-10-01 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c4544ea0-b21e-35f7-afe2-a06b2d855642 | -11.843 | -45.0104 | 2025-10-01 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 29c8ceb7-4f72-3401-a3c0-66559512d034 | -14.3714 | -45.9172 | 2025-10-01 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 51008f6f-99fa-3ccd-8c5b-c19954162674 | -7.8002 | -46.7578 | 2025-10-01 11:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| cfdf710b-f26c-390c-bd9e-e68bc72b39e5 | -10.9773 | -46.5217 | 2025-10-01 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6531ec40-e036-322f-9abd-4d18b4530b13 | -11.8482 | -48.0595 | 2025-10-01 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 71d4d428-b339-30e5-bdee-c9411ecdabd9 | -11.9254 | -48.0051 | 2025-10-01 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d85a22b8-1614-35a4-9b60-2ff8d6747615 | -14.9733 | -46.8896 | 2025-10-01 11:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 6674bb91-16d6-3d70-8bb1-d390f3facaae | -14.8016 | -45.8178 | 2025-10-01 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8df1096b-e2ff-3718-9f87-269f592d3c94 | -14.3519 | -45.9206 | 2025-10-01 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 35f7ee39-26b5-30a9-a066-b81f2ed613ff | -14.8021 | -45.7946 | 2025-10-01 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9a12d2e1-11c8-3885-9978-bd5377060492 | -14.7836 | -45.7516 | 2025-10-01 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6380d901-7400-3089-9204-aa856b87f835 | -10.9769 | -46.5443 | 2025-10-01 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 40efab0b-6f9a-3aa4-a097-5f66b569e9eb | -11.8622 | -45.0075 | 2025-10-01 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0099bdda-c3bc-3143-b7a1-3fb43c1e4536 | -6.32741 | -43.02465 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 90060b95-9916-3481-a12b-08e8259b1971 | -5.9661 | -45.86813 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 520aadfb-ccc9-353e-942c-44e57ce57d94 | -5.15683 | -43.7121 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 787a5e35-5896-330a-9db7-5324156e9183 | -6.39321 | -44.28228 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 46e356e1-c3dc-380f-993c-0e67f9f2da84 | -5.80769 | -43.7402 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ce0af1d1-3833-39a1-b562-d2553e18c817 | -5.68264 | -42.63451 | 2025-10-01 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 59d3b21e-8e6f-333b-9519-30d7205fa286 | -7.41943 | -41.85201 | 2025-10-01 11:57:00 | TERRA_M-M | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1be4ad20-69b9-3fd0-9da6-683754427030 | -5.27407 | -42.78164 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9d79577a-a184-353d-8f7b-46d6663d433d | -6.36221 | -44.58926 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 1548010f-78e8-3c9b-aca1-60f8f7a7f52b | -7.39389 | -44.60796 | 2025-10-01 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 4bbcd994-1493-3df1-ab18-b7f8047caf4a | -7.78552 | -42.5132 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5862bddf-d1db-3cb2-8172-3badee577498 | -3.68934 | -42.57551 | 2025-10-01 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cdc52cf4-5dec-3579-afea-09c4d53dd7f3 | -3.92475 | -41.57973 | 2025-10-01 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| da5d2770-06df-3ca8-b44d-795ad4c25b43 | -6.08065 | -42.43385 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 582d23d6-6d52-303d-8053-54ca9a37d383 | -6.5072 | -44.2391 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2864dc1f-c519-38f6-9c40-263ebfb09cb8 | -5.68394 | -42.62557 | 2025-10-01 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cfb219f7-5a14-38a6-96b0-08f8398fe4ed | -7.63543 | -45.45196 | 2025-10-01 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d2dde573-92cc-397a-b13c-17fbe46b900f | -5.62308 | -44.37241 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 526480ee-b0b2-3565-a329-af3b3c1e07b4 | -6.50668 | -42.48914 | 2025-10-01 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 880b9959-4667-395a-aa8c-b88744fac5fc | -6.39172 | -44.29248 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8e12be08-427d-3f26-9d9b-6bc8766fe099 | -5.2526 | -43.75232 | 2025-10-01 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3751b17-7b93-36a5-9523-b0c9f3276300 | -7.14988 | -43.70517 | 2025-10-01 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 55c500d8-061d-3e6f-85d5-2fd2fed8c0cd | -6.40492 | -42.80523 | 2025-10-01 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 09b7d0fa-68c3-3b41-b2dc-66efd4a58ead | -5.95367 | -45.87941 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f35387ad-d176-351e-8fcf-4a6696c16f3d | -7.17356 | -41.69952 | 2025-10-01 11:57:00 | TERRA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| cbdb5130-1496-3ab5-bf1f-097e3dfa35c2 | -3.3505 | -43.19177 | 2025-10-01 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fb410ae7-11c1-3bb7-9afd-c282fd9d02c8 | -3.95759 | -41.68 | 2025-10-01 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8682b04f-7420-38f1-9e21-fb542931043b | -6.27554 | -44.06425 | 2025-10-01 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5fa6eb9b-652f-3731-a1e0-ab8f00c69397 | -4.92193 | -43.29753 | 2025-10-01 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 72ec6a65-f30b-3d4e-8fa0-50af1c631a10 | -5.88492 | -42.51162 | 2025-10-01 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2272dbbc-dee6-3210-9058-2a75609cd752 | -6.3638 | -44.57872 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 1efe4d46-dbdf-3907-817b-c9e8c91360e3 | -5.32143 | -42.76986 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b1ab644d-36ec-3154-b7cb-322973cce89d | -5.49803 | -42.76115 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 6c6553b7-cfd5-3869-af8d-8d856c80ba21 | -5.27102 | -43.18081 | 2025-10-01 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |


[Clique aqui para ver as próximas entradas](README140.md)
