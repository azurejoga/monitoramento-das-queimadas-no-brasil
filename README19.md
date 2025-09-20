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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ba09a90-fab8-3e81-89cf-0d3792b440b0 | -25.09112 | -49.38395 | 2025-09-20 04:32:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f753137c-1652-3049-aa7d-71aa457a8a46 | -22.80354 | -45.27552 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 88ee6832-4242-3522-a63c-415146f3e5c7 | -22.62056 | -47.71011 | 2025-09-20 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5be8a1c6-1547-38df-be75-838053dffcb1 | -22.92985 | -49.59633 | 2025-09-20 04:32:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4c5f90d9-6c9e-3fa6-8f6f-83ee7d84b43e | -25.24983 | -52.19949 | 2025-09-20 04:32:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3d3f795-5fd3-3d1e-b3b3-409ef489e798 | -23.29081 | -45.78069 | 2025-09-20 04:32:00 | NOAA-21 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| fa98f411-9735-3766-8c4e-0f9e5ee2e980 | -22.62773 | -48.26935 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d5f05e8-c771-3236-aa48-960274f62b78 | -23.81443 | -47.56573 | 2025-09-20 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67c8944e-63a8-3f91-9bfe-167fd27f0c41 | -22.6249 | -48.26475 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e7fffc1-057a-3595-aeea-5945db156c7c | -25.0445 | -49.23012 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d15a45bd-dcf5-357c-9770-d9791bddcd6b | -22.18179 | -55.99646 | 2025-09-20 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1ff578b-8fc8-3c27-8566-b4a8a7f36653 | -25.09449 | -49.38451 | 2025-09-20 04:32:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c756b39-78c9-30a1-91c0-b09af84cfdae | -22.61997 | -47.71426 | 2025-09-20 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 71359d17-62f3-3f81-91e1-03dfed078870 | -25.89181 | -52.17147 | 2025-09-20 04:32:00 | NOAA-21 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5f03f89b-fa22-36a3-8245-1847f4aacf31 | -22.1859 | -55.99734 | 2025-09-20 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d14ecede-173f-3f50-96ae-5932d25e48ad | -23.18387 | -50.93294 | 2025-09-20 04:32:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29922bb0-267d-3766-bcbc-7313b49eb461 | -25.04336 | -49.23797 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a8c0a8d9-2ae1-3ab3-ad9e-457842dd1954 | -23.81384 | -47.57004 | 2025-09-20 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d63875ba-52a3-3aab-8c68-c39575ef9f4e | -25.04788 | -49.23065 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46e8f2e8-14d8-35a5-ab41-5d786301d7f8 | -23.13941 | -49.6483 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4632ff15-617e-3903-89cf-5260ad89a921 | -25.04507 | -49.22616 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 343b2bac-c5de-374e-81e6-b2243923b819 | -23.28054 | -46.40165 | 2025-09-20 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a81f96a2-1b3a-39a7-83fa-b22cc2cb4d21 | -23.44038 | -47.61018 | 2025-09-20 04:32:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7d3679e-198f-3f2e-9111-68a943b55c21 | -23.81973 | -47.57972 | 2025-09-20 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c70ad746-23e7-3083-bebf-e96be81acf10 | -23.53448 | -46.25409 | 2025-09-20 04:32:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 908886d9-7c24-3862-9ca5-06ed8d868376 | -28.06139 | -48.67341 | 2025-09-20 04:32:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| edf9167b-29ed-3fd6-8916-edab282ed3c4 | -26.75451 | -50.61449 | 2025-09-20 04:32:00 | NOAA-21 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6229ec41-ed04-3249-ab6b-c373eaca73a6 | -22.42813 | -48.56279 | 2025-09-20 04:32:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5fae3ef-fb1c-368c-bdbc-7d3e2ab1c8c0 | -22.46696 | -49.01371 | 2025-09-20 04:32:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05296e43-4203-39db-8b27-6abc16a2560a | -22.6195 | -54.95042 | 2025-09-20 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 68b4f58d-dc07-3247-a153-16024bcb02a5 | -23.14273 | -49.64892 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f923dd5f-43b0-325d-b738-0af77320d6cd | -23.20088 | -46.21179 | 2025-09-20 04:32:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 458b771d-e2b0-3346-a466-2e73dd254f6f | -22.44137 | -46.88998 | 2025-09-20 04:32:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f35da685-d0a6-341a-a65d-88200f1a86c0 | -23.32283 | -45.97931 | 2025-09-20 04:32:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a34ec20b-c435-3cde-a8c4-0c79878922b1 | -23.14398 | -49.61811 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0186cad-7fcb-3e50-9a78-dc26f61809cb | -22.80286 | -45.28092 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| cff4aaa2-a92e-3525-b0a0-454610b07fd6 | -22.6391 | -48.26314 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c27de880-0899-3531-8d67-3587d5bdd8bc | -21.29593 | -54.79405 | 2025-09-20 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5459725-fcc9-311a-91af-90d79c4246fb | -22.19439 | -49.64993 | 2025-09-20 04:32:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 040a1d17-3da4-3a32-a782-c19e8d73f742 | -25.02515 | -49.33963 | 2025-09-20 04:32:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a61486dc-26c5-38af-8599-7a8f25f80f9a | -23.20619 | -50.25252 | 2025-09-20 04:32:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4ec2538e-612c-3f79-be82-9e59e7fc1837 | -23.21553 | -50.25806 | 2025-09-20 04:32:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0f88b206-15a8-3a8b-bfaf-f4bad08a3573 | -22.64194 | -48.26768 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbb5e907-344a-3886-977c-d64e1fa7f88d | -23.3315 | -49.34347 | 2025-09-20 04:32:00 | NOAA-21 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d0f040a-0a0e-3310-83e0-ceffd6e4b1ce | -22.63853 | -48.26711 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 910feb04-93d9-311d-a2b0-e445577722d3 | -22.8068 | -45.28151 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| d4427073-45fa-322c-9928-1e41e6c5ab53 | -29.73897 | -50.5615 | 2025-09-20 04:34:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2e300f79-3fb7-34c0-8c10-e074759b24ba | -10.26216 | -36.33662 | 2025-09-20 04:44:00 | AQUA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 549916c9-b2e7-3fa6-abca-c78d9381870a | -0.91349 | -47.55101 | 2025-09-20 04:51:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6deada5e-fef5-327d-92b3-34ff3ae4211a | -1.27229 | -47.86937 | 2025-09-20 04:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b59bb1-daaf-327a-af1f-80ceb5a62fe2 | -1.11491 | -54.09194 | 2025-09-20 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a231c7ee-df8e-335f-b06a-218db25389e3 | -1.17973 | -47.79383 | 2025-09-20 04:51:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce46bc29-7ac4-32d7-9339-c12435720ffc | -3.6543 | -41.1193 | 2025-09-20 04:51:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5dff08a-1b9d-3d1e-a79d-3e49262fbd52 | -2.26382 | -47.84472 | 2025-09-20 04:51:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3bff30b-033b-34a1-9418-9e47b908a87e | -3.65496 | -41.11477 | 2025-09-20 04:51:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd4f78ca-6a22-3b84-a24f-a2472d7c980d | -1.11845 | -54.09251 | 2025-09-20 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea5f8926-218d-378a-814a-404d4aacd926 | -1.16898 | -54.14091 | 2025-09-20 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af264eab-878b-3a43-8341-029cd7aecabe | -1.17165 | -54.14038 | 2025-09-20 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14ca76d4-87f6-376d-9249-9ab5aef8155a | -1.7608 | -48.05161 | 2025-09-20 04:51:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c9d97e-d953-3cbc-b83b-ce0f7d3d856b | -1.26857 | -47.8688 | 2025-09-20 04:51:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1449db30-f4a5-3524-ba36-b189e1199c90 | -2.33149 | -48.6195 | 2025-09-20 04:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b215f26-6fad-36a1-9f9e-f39ae2fd15a9 | -1.1944 | -54.22586 | 2025-09-20 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84bb9987-0333-3306-acf4-1a7ecd20359e | -2.3014 | -48.14784 | 2025-09-20 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50f4241-ef67-3009-ab10-a06f03143ac6 | -1.54334 | -51.64758 | 2025-09-20 04:51:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a53911-6d17-3b92-a8ae-23d5a4997995 | -2.13256 | -47.99826 | 2025-09-20 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747d1d2a-52ee-3c26-8e8b-1d3dcf38588f | -0.91407 | -47.54894 | 2025-09-20 04:51:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15c8370-b1c6-3fb7-a783-f0740445ef51 | -1.68886 | -48.19907 | 2025-09-20 04:51:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e254b6-5304-34ab-a359-ed7c3c577c0f | -2.38252 | -47.63049 | 2025-09-20 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3251b4-9554-366f-b174-4500fc0d07f2 | -5.11384 | -43.20715 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb222096-dfa4-387b-9ce3-c1516e82a0fc | -9.17268 | -44.62989 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d1c34fa-aac1-3358-a4b8-d7c7836f3e45 | -5.76187 | -53.41764 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d479a335-ca9f-35f4-8f3d-1aad55211827 | -6.60994 | -43.58851 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46fe9af8-815e-34bc-85d8-29de657aca84 | -7.92092 | -43.88342 | 2025-09-20 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 854cd62d-269d-36ea-b327-d6e7201f837c | -5.11127 | -43.20802 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7cf6b223-410d-3c37-ab2f-366cb37f2cfc | -5.83861 | -46.28359 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf4c1ea8-ad20-34ce-ac0b-15c47a517c26 | -5.80655 | -53.43929 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97466555-ffa9-31a1-8ac8-07dcbbad97c9 | -5.96447 | -42.91587 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d0bcef7-bb47-3d54-8260-6747aba59327 | -5.79077 | -43.64436 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9631df60-0aa7-3fc8-86dd-e542bc856d0f | -3.97263 | -49.96856 | 2025-09-20 04:53:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28382db8-38d9-39ce-a708-765527cd357d | -4.86909 | -46.83301 | 2025-09-20 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b64c85d-b14c-39ae-9c51-69961a30cf4d | -6.22289 | -55.6374 | 2025-09-20 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f0f60d8-3a13-3823-8562-80bc0c797660 | -6.1023 | -47.85521 | 2025-09-20 04:53:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c3bd0f-c4b4-38c2-b5a3-e7cb1444f0cc | -7.59489 | -45.48868 | 2025-09-20 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d46a37be-05ed-3b1a-9387-c978acda4dce | -8.14424 | -43.63792 | 2025-09-20 04:53:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba2c481a-7193-388f-920f-bb364e00da5c | -8.19438 | -49.67277 | 2025-09-20 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2623476-37ce-38ab-a61d-cec420504448 | -2.79552 | -47.15272 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 231d6036-f5a2-3e18-b539-fa2f42d66e7e | -3.62083 | -51.79292 | 2025-09-20 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a83eee9d-54ad-3a2d-a1b9-821789104b55 | -4.36041 | -46.28854 | 2025-09-20 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a814d22-5d7a-30ed-99e4-6795c57a1ecb | -8.89782 | -40.43923 | 2025-09-20 04:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c243209c-a2d6-3c36-b7ca-b7fa41f0f9d2 | -7.70941 | -55.19203 | 2025-09-20 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f619a96d-ac58-353f-b5a1-1c9c177c725b | -8.19502 | -49.66849 | 2025-09-20 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b7b7bc8-7716-38ce-a3d3-aef98de4afbe | -5.11433 | -43.20382 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e7933d2-faad-3b9d-9472-cbbb1970f618 | -5.10258 | -43.20921 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0497969c-ca21-3ba0-8111-ea5da64496ac | -2.51702 | -51.9065 | 2025-09-20 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d6baaa0-8965-3b4e-ac98-95ed8ec34cb2 | -5.76522 | -53.41819 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 982cf334-5754-3152-8f92-006f883f027a | -3.51367 | -49.44585 | 2025-09-20 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 723a25a4-160f-319e-b232-2360ac2cde62 | -2.63571 | -48.99453 | 2025-09-20 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09f6f543-3dfd-320d-970a-d9ab4fb560ba | -7.83194 | -45.63391 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21238e66-84f1-3fdd-8341-72fefefc9b9b | -3.51306 | -49.44976 | 2025-09-20 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cf23ac3-131a-3b97-ab06-2dfebda273a7 | -5.78899 | -43.65723 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README20.md)
