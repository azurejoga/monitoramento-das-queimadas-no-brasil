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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01006940-2c3c-3f85-a5ad-f823a97b007f | -19.74412 | -42.00629 | 2025-10-01 04:53:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03caf78d-0e77-3d3a-a64a-c63982f16ea8 | -17.67473 | -47.2652 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aff63c4f-afdc-3e8a-b339-f9cdf705a9da | -15.86527 | -59.31504 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de852dba-c409-3612-9a61-87bcf22169c0 | -20.63158 | -46.2088 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6661716-40dc-321b-af65-16edfcd468b9 | -16.24771 | -50.94251 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1de17210-e2c6-31a1-bbde-1d260a369a1f | -15.2737 | -56.77449 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8f7d28e-5e05-303e-a8dd-7aa07d2fb592 | -18.7138 | -43.17811 | 2025-10-01 04:53:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5016a552-bb1e-36ab-829f-98c23f330cc0 | -19.16446 | -44.53094 | 2025-10-01 04:53:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f8abe50-8065-3f30-94fe-450f5005e3fd | -18.32432 | -44.77311 | 2025-10-01 04:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75aac622-0421-30bf-806a-f37177b6d441 | -23.17973 | -45.47575 | 2025-10-01 04:53:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f4a2d68c-70de-34b1-9b43-03ec0c08d166 | -21.6621 | -45.34114 | 2025-10-01 04:53:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1dfa2a7f-0927-338c-800e-8c4474c9c531 | -20.61801 | -46.19682 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b8029df-0840-30a7-b2d2-14c1ce443f6a | -18.90597 | -48.06605 | 2025-10-01 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c681ca53-25db-347b-b12d-35cf15934d03 | -22.58187 | -46.77959 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 8e0d9c0c-bb48-345f-bb43-f797228ca583 | -20.62734 | -46.20227 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 508e9b43-49d6-3428-aa9d-e9e6d6c676b9 | -20.32796 | -43.04325 | 2025-10-01 04:53:00 | NPP-375D | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 76683e85-06f9-3896-a27f-0cd8155ae301 | -22.43654 | -48.31041 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 07fc303d-9181-3eef-bef6-d70745a7c55f | -18.48622 | -44.03719 | 2025-10-01 04:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f8a894e-78d2-3d13-be06-23040ee90beb | -19.81083 | -44.07396 | 2025-10-01 04:53:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27045bfe-002a-3bf4-960b-4eadc9488ef3 | -23.19621 | -45.10781 | 2025-10-01 04:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88d8ed84-447c-3a8d-941d-ea6d80095e35 | -19.83909 | -46.71738 | 2025-10-01 04:53:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f48d650-383b-3326-9228-bb2ba8e74e19 | -17.62102 | -46.70049 | 2025-10-01 04:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21f7d8e8-3792-3cbe-8b99-a70a3b8a9e99 | -19.8285 | -43.08745 | 2025-10-01 04:53:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b8129ee6-b332-38fa-8231-d64ac48c633a | -20.47647 | -43.94782 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89667a7d-28cb-35e4-97fd-fc8cf8850e62 | -23.21313 | -45.11168 | 2025-10-01 04:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d0850e0-54ba-37b6-bf75-c76e95b1f2c6 | -22.11393 | -44.7031 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ca6d62b5-c519-394b-a5af-d6c59757e918 | -15.28436 | -56.7892 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e7f7042-0861-317b-a397-c57c55b3ff4b | -16.83105 | -48.85156 | 2025-10-01 04:53:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a69fcf75-5369-3634-af49-ce094ba5194c | -22.58129 | -46.785 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 3da04ba6-034b-372d-b354-2cc9971dd458 | -17.96774 | -45.02508 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e0b4d63-163f-32be-8646-9940f56d8487 | -22.25803 | -43.42702 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 828bfaf1-eab9-3680-921d-f55cd6f3a08d | -20.47879 | -43.95369 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1c1cdf07-854a-3c0e-b09a-fdab38ccc85f | -22.11425 | -44.69968 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 648d5e35-2f94-3ff5-ab9f-ec5471a6a467 | -18.49171 | -44.03787 | 2025-10-01 04:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f391a7a9-2aca-3e07-8d42-e885b8001c4a | -16.53717 | -50.27533 | 2025-10-01 04:53:00 | NPP-375D | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52d01acd-2f5a-3868-bda7-0470e90d9318 | -15.34559 | -56.9661 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e3172420-59e9-3e3d-8079-a96f2cc6ceaa | -22.09727 | -47.8027 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d73e520-15c9-3339-a4b4-8c7f55c5b8a8 | -16.25529 | -50.93961 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddab7331-8f64-380f-8304-b7b58674f74e | -19.88537 | -42.62887 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dabc4476-163c-3233-b531-70cc43d011f1 | -22.06055 | -48.3314 | 2025-10-01 04:53:00 | NPP-375D | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0af49509-ff5a-32e0-a0d3-12c2f12d074e | -15.51525 | -56.19413 | 2025-10-01 04:53:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 650a88d2-89bf-3e58-9010-1aefe5ade494 | -18.60473 | -43.26945 | 2025-10-01 04:53:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ff075499-fd42-3e3d-a8d0-3a7fef2f8ae5 | -20.03052 | -44.53922 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ecb59ce-60a6-367e-b6ca-0f943d977d61 | -19.6934 | -43.68525 | 2025-10-01 04:53:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86add017-ba3c-3c9d-b414-ef1128b8b431 | -18.80893 | -47.55554 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a92db358-f54b-3432-b090-a41a276d7495 | -20.63087 | -46.2152 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd2d2c83-9398-3667-a04b-fa3b0f9b6019 | -21.66243 | -45.33779 | 2025-10-01 04:53:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 73dbd4bf-0593-3a31-9041-ed0b35704a08 | -15.84901 | -59.60053 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b8c0f92-5f97-312d-b3e8-934ac9249720 | -18.71171 | -49.17061 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a930d7a-a90b-34be-b95c-1d9f6dec9d67 | -18.15957 | -46.10416 | 2025-10-01 04:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3b11381-3883-3738-995c-b4f59f804512 | -18.41328 | -53.22053 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e26b49a-bc9e-3655-9428-ea83b03c8c6c | -17.21097 | -46.98342 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e0f270a-ef2b-374b-8f73-3b65f576f61a | -22.26985 | -46.71619 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 32469f61-c7e1-3be2-b7ef-39cee8946938 | -19.86204 | -43.82368 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d6da638b-14d3-367f-84e1-bfda0d99bd8a | -22.26508 | -46.71496 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1637a839-d1bd-38e6-9a56-a43317b14feb | -17.2791 | -44.91663 | 2025-10-01 04:53:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25685a1b-7a59-320b-939b-9cdd8bb33411 | -15.34184 | -56.9655 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1472b9-b070-3772-b725-45f7e22c3f6d | -15.84892 | -59.59758 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 114fe528-94d7-3dde-8b43-a5e9634f2e6e | -20.5866 | -45.87998 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12c7e4a2-13a4-3ae1-ba80-7bcb1dbdc061 | -15.84034 | -59.59878 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fe76af7-8b66-345d-a573-73bb601088b3 | -20.33392 | -43.04401 | 2025-10-01 04:53:00 | NPP-375D | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 83d4a925-9430-39b4-b7b5-fbc12769d23b | -21.04074 | -45.68084 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c84c9ce9-73dd-3b71-8af9-f4581255a3f6 | -15.27001 | -56.77374 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e52491-eb4b-33cd-9e32-614e8cdb3df9 | -22.11457 | -44.69628 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cdabba40-a265-322e-8ff4-95cca0645dc6 | -18.41719 | -53.21742 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50ea5d8b-286f-300f-b9b1-1431bcd84c8f | -20.59181 | -45.88453 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bbf79f1-73ad-3826-ae27-26c56587583f | -20.59667 | -45.88058 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e516184c-ea42-302c-a70d-641670464f66 | -17.28421 | -44.91729 | 2025-10-01 04:53:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a19a7cec-56c2-320d-ad6b-dc717d97d39c | -20.59606 | -45.88644 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6c1acdd-673a-3d83-a765-85f1186815fb | -18.71421 | -43.17401 | 2025-10-01 04:53:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 54ad00e0-2521-3b84-9952-5ed27389481b | -17.97287 | -45.0256 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c81c786-a8ce-35e8-a085-be4fc3c5387a | -22.43552 | -48.319 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eb620339-bebd-3bcc-868a-2c5c2169cbb1 | -15.28225 | -56.7795 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d3f9848-28d7-37e6-b193-4079a0061578 | -20.23467 | -43.88578 | 2025-10-01 04:53:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f049b5ea-c799-3c12-87b3-2351ecb1fda6 | -15.26561 | -56.77711 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec5e4496-3742-34fc-a1e9-4901bae6bc6b | -22.25206 | -43.42654 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 801042ad-e0c1-36f0-af13-1941aed0fcef | -22.92456 | -45.50801 | 2025-10-01 04:53:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccddd12b-5212-3d0f-85d8-490cebfb1c7a | -17.67924 | -47.26004 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31efe85a-2acd-3584-a1fb-ed2c709ff2e4 | -19.16183 | -44.52786 | 2025-10-01 04:53:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3280ab4-2dff-3409-b369-d0a630ecf7d5 | -18.91881 | -48.16821 | 2025-10-01 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0079ac84-3bd6-3463-bcd1-5282fa2c618f | -17.40207 | -47.16562 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edcc72c2-f5d0-3f2c-9473-f1415e169019 | -19.8655 | -43.81846 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f9fe546f-fe98-3802-a680-0ba0a3fbb46a | -23.21217 | -45.11282 | 2025-10-01 04:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97c91783-d6c6-31b3-8abc-221372677082 | -22.98221 | -48.35258 | 2025-10-01 04:53:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c54b89bd-2d3e-3f89-89bc-16926a604d22 | -15.24094 | -56.80947 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7733bf3f-6c55-3e78-ab18-de547f409ffd | -20.64012 | -46.22131 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 257d9d18-f696-3bc9-8311-bcab7f109b58 | -20.3343 | -43.04004 | 2025-10-01 04:53:00 | NPP-375D | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d03d7cc4-5598-3f22-8464-2e6e2420b5ad | -23.19649 | -45.1049 | 2025-10-01 04:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd7f94d2-d7a2-3b3f-9394-3ddd4df1a7c1 | -20.60521 | -46.22303 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a81c2b-8c49-3940-a1f8-12c105592e23 | -18.48653 | -44.03421 | 2025-10-01 04:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015955c3-d3de-355e-8b29-00872d3debc8 | -22.4093 | -43.16631 | 2025-10-01 04:53:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 755cf6f0-37ef-3c69-8bad-ccb58683ea2d | -22.11551 | -44.6862 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 126ee9d5-adce-3f78-8fe8-edc1f392d8ab | -20.60189 | -45.88507 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c72f603-f743-3c7c-b513-9efb19af14c2 | -15.84468 | -59.59966 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f1bc7e7-74fa-357c-9f5a-89c51a4bbe39 | -22.28612 | -47.73652 | 2025-10-01 04:53:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb592ebc-acc7-3c61-be2e-dc3af9d1fcc0 | -22.64608 | -46.75527 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b5c2f68-dcdb-3bf7-ac21-6c13c7f8e2aa | -22.78524 | -47.22266 | 2025-10-01 04:53:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a2ffc7d-54e9-3c82-97c9-13e0ac4a3a8f | -18.69994 | -44.33112 | 2025-10-01 04:53:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05167f35-41da-3e96-ab5c-64ae892ded64 | -19.86238 | -43.82014 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d8d95b45-e753-3135-be65-1e29344a0647 | -15.29618 | -56.78711 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README116.md)
