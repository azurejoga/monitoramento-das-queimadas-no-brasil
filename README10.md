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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1ff00c8-32cc-32ac-ad61-a3744a4626ee | -20.12934 | -46.88139 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfc8e72-e427-398d-984f-43bee789d479 | -20.25194 | -47.79347 | 2025-09-14 03:30:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44fe8359-17ad-38b1-b225-7123627c4adb | -17.27817 | -46.11122 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc6a47b6-3327-3d0c-ade9-ca4d5cadac4f | -19.99772 | -46.90218 | 2025-09-14 03:30:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db7d0a98-539e-3607-84ad-f8f32066858d | -22.49428 | -47.418 | 2025-09-14 03:30:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a296092e-e1e9-3bf3-9fb9-8a013deb190c | -17.31833 | -46.0873 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96610736-1464-3564-97c4-dede63326eba | -22.20573 | -48.35821 | 2025-09-14 03:30:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a0e5ee2-d92d-3050-b02c-01e6eb66f8a5 | -22.20713 | -48.35265 | 2025-09-14 03:30:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5ff1fd0b-d5e1-3ef3-8487-e90302010ac5 | -20.78735 | -44.91003 | 2025-09-14 03:30:00 | NPP-375D | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 00a29854-4fd4-3e7a-abcd-cef5c4eb752f | -17.27518 | -46.12412 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33940524-3c66-3d1f-b29b-8d3244c2d148 | -22.20024 | -48.35143 | 2025-09-14 03:30:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88278de7-3214-3fce-b2e8-89241e11eba1 | -17.27181 | -46.12151 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3d67df7-e5e6-34fe-8ed0-ab55bfa45b3f | -17.28105 | -46.09886 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b36ebc7-5dc6-3c36-9466-6baed9658917 | -19.09734 | -44.49394 | 2025-09-14 03:30:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf241477-b295-3820-80f6-ae645d3f6fe4 | -19.71138 | -45.44255 | 2025-09-14 03:30:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0fa7e49-d0b7-34e6-9d51-081c64db325c | -18.37982 | -48.34966 | 2025-09-14 03:30:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cbbc1413-4e17-34b6-8402-9a29de5473b7 | -18.01449 | -46.95294 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c58ff2b7-433f-3462-8ea8-488f920265e1 | -22.22051 | -48.61715 | 2025-09-14 03:30:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e3b4ac6d-5f8c-3466-9459-a15f175eed0b | -18.25965 | -46.95008 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d05aae9d-136d-30c2-a04f-1c821d954361 | -21.07652 | -47.11819 | 2025-09-14 03:30:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85add533-d2f6-352c-8fa9-da6931f161a0 | -17.26667 | -46.1136 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 929c6e0f-51de-33a0-978c-ca3075706d04 | -20.08811 | -43.21227 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bdecf251-5eb6-3f9f-b10f-4b08b251e099 | -18.01109 | -46.96741 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4aab67fe-94bb-3235-a1dd-0c7afd8ad9b9 | -20.09133 | -46.90378 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecd13189-1918-3e88-9b4b-c127a99d3555 | -21.30222 | -48.56256 | 2025-09-14 03:30:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5755a028-e23b-3dca-8c84-5f2e9d5d3d7c | -20.25249 | -47.79405 | 2025-09-14 03:30:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd0c4a81-93f3-3b99-a7b1-9e4cc5701c4f | -22.22757 | -48.61298 | 2025-09-14 03:30:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2f7f03db-3c97-3b0e-b51f-e1b0055cef9d | -22.29098 | -45.96926 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9784cc45-e6f5-39bc-9687-cb52dc4516f9 | -21.62347 | -46.81074 | 2025-09-14 03:30:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e5e170df-1bf9-3552-a85b-6057bf2b6102 | -19.09156 | -44.49252 | 2025-09-14 03:30:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee18f52f-4364-3775-bdaf-cc914917d449 | -20.0847 | -46.90264 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57916c2c-a7fa-3376-b00d-e41ac97b473e | -19.70603 | -45.4405 | 2025-09-14 03:30:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dabae33c-ee65-379c-b629-fe18fbac3651 | -20.12416 | -46.87434 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51db7811-24dc-38ff-9d30-ea275eda99c4 | -17.31332 | -46.09077 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a229859c-1b8f-36e3-9108-b74d19efb939 | -21.07494 | -47.11751 | 2025-09-14 03:30:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1020ab48-52d1-31b1-b1c7-b6c46df3ec96 | -19.70647 | -45.43619 | 2025-09-14 03:30:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc9d5856-49bd-3c3a-84c7-0fb4523160f0 | -20.00008 | -46.90977 | 2025-09-14 03:30:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c70132f-019b-3681-93b3-c1ecd5b40aef | -21.07628 | -47.112 | 2025-09-14 03:30:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9da1610-6b75-3f0e-8224-3d4715497a61 | -18.19303 | -47.91809 | 2025-09-14 03:30:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d356d91a-c6e5-3d76-9bf7-ca28f6d3706f | -19.9938 | -46.90713 | 2025-09-14 03:30:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f7d8a89-6b6d-353c-a99d-fb64933089a5 | -17.28419 | -46.09735 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 975ef9b8-1863-3ec7-a8f5-e6b213f0e2f8 | -20.12455 | -46.87983 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81685fbf-a8de-3b46-9962-7057b3902361 | -20.44525 | -45.24616 | 2025-09-14 03:30:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b3aaaf5-b4b8-3b45-a27e-9392c2a4b159 | -21.76545 | -45.4576 | 2025-09-14 03:30:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 27ed3415-97df-3415-b7ec-f33216c3db26 | -17.31486 | -46.08389 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7328b2a4-12a1-3b52-b52a-e40bd0b1a0ba | -17.27604 | -46.10278 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9184eb8d-f976-3370-a92f-51004aec7c1a | -21.92141 | -46.55439 | 2025-09-14 03:30:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bcea027d-f83a-3bce-b470-cadf3e3f49e0 | -22.28508 | -45.96769 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 625271d0-1df1-3aa9-ac0c-3d2bb4e6471f | -20.08962 | -43.20534 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a089dcc-111d-3e00-af6a-33063e0655ee | -18.37405 | -48.34357 | 2025-09-14 03:30:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 06ead2b0-f18e-3288-9f2c-5353c54ae982 | -18.00939 | -46.97467 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe2f72e5-c1e0-3fa2-a71c-56a8293a4501 | -19.14624 | -44.84489 | 2025-09-14 03:30:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e19e1710-cd34-361a-9bb3-8ce49bfcebb2 | -17.9923 | -46.9557 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab1f4d68-6fcf-30ce-a91c-4d2614108081 | -21.30402 | -48.55537 | 2025-09-14 03:30:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3aaae634-c456-3cbb-85e8-968504eb0903 | -19.67323 | -43.12199 | 2025-09-14 03:30:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96101771-1ca4-3773-ae8c-256b00704e2e | -17.31518 | -46.10099 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f3bae73-b9c7-30da-ab68-8d4752c938a6 | -20.08887 | -43.20879 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f29858ad-3b05-3fc8-a246-a2fdd1d4915b | -21.62203 | -46.81673 | 2025-09-14 03:30:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a83199a-13b0-3d35-a8df-c597d8c0c8ab | -18.26054 | -46.9445 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89640cbd-2a0c-35c8-a33a-34a77be979c8 | -22.28333 | -45.96506 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f41ee39c-4237-3123-be87-de7497a59cc3 | -22.28231 | -45.96941 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 36a30215-d858-338c-8bf6-360351b0b90b | -21.76438 | -45.46216 | 2025-09-14 03:30:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 54268d8d-ce89-3ae6-94cf-97746f1568f2 | -20.25089 | -47.80069 | 2025-09-14 03:30:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d611b2-3fd7-31ac-a1eb-9615150e73c8 | -18.58857 | -47.20139 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e6c7390-81f0-3b43-8800-b8f65134b512 | -22.72242 | -49.89676 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75e765e5-9e94-38fb-8fbc-e315c53dd796 | -22.72723 | -49.90793 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 543e74c6-4cff-3855-b735-9bb7a61310e6 | -22.73664 | -49.90155 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1d637a3c-4d7b-3070-8db6-d4370ae2868f | -23.79611 | -49.94627 | 2025-09-14 03:32:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e71db761-7872-3c30-816c-b17e6a73af14 | -22.72754 | -49.90503 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c324d659-f801-338d-8b69-3cbe55b84886 | -22.72943 | -49.89954 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4d1ecdb6-150c-3f60-847e-d6847933dcdf | -22.73473 | -49.9071 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9722240-6b33-31f6-8bb6-59b4debc9c3a | -22.73702 | -49.89856 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6c8ec1cb-accc-33a5-bf47-166580831d75 | -23.6593 | -47.60075 | 2025-09-14 03:32:00 | NPP-375D | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2a50257b-0c89-39c6-b66a-7ca21e14bfc7 | -22.72276 | -49.89392 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02d36823-767a-3213-8f07-7241359b0dcb | -22.72981 | -49.89654 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 02cb23c6-e15c-37e5-a1a9-1d967aafb966 | -22.73162 | -49.89113 | 2025-09-14 03:32:00 | NPP-375D | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 038094ef-2f82-3e70-803e-fdf0e4f7513d | -11.4453 | -50.7549 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 858378ba-33ca-37ae-85c5-0f7a463dee3a | -12.8055 | -48.0182 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ab3b535b-5f35-3c58-b6d3-d7b6555dc4c5 | -12.7867 | -47.9986 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 113c6912-2fa7-3667-becc-b7b98594d10d | -12.8059 | -47.9959 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9974cd74-6fe1-3be8-8cce-95cc36bcf72a | -11.2885 | -51.1122 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 10708f7f-d6d1-3a21-bfac-899e9df9714c | -11.464 | -50.7741 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c53cd06c-1c46-3958-a2b0-aa3af74692b8 | -11.4833 | -50.7507 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a0919a61-648d-3607-bdc3-cb8bb4fbbf28 | -12.8019 | -47.1474 | 2025-09-14 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1ea8c405-1ef5-30ff-8664-ad42151bc7d4 | -12.7671 | -48.0236 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 62798dce-c2a9-377f-8124-878027bc1f4d | -12.7675 | -48.0013 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| c6327e19-a808-3a9f-b0d7-ec2508985d94 | -11.4643 | -50.7528 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d0719126-176e-37ef-952b-0192c01f6e62 | -11.483 | -50.772 | 2025-09-14 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 83e85745-4509-3ce2-9312-c3dfb66bd7ae | -12.7863 | -48.0209 | 2025-09-14 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 214.0 |
| a49afa09-31c4-3a31-8942-e529c3311e4f | -9.05797 | -47.03068 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0806ae6-d7de-33a8-bc90-d52488c02af1 | -2.25935 | -47.85498 | 2025-09-14 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f18a5820-ec1c-3740-8343-fef8f3e80725 | -9.48359 | -46.40697 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12d1926e-e477-3d1b-bf51-be7c8f418028 | -10.13021 | -46.15868 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5ec5974-01f0-3713-a931-e4339a7ce72b | -9.75028 | -46.87362 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c44b21c-6a3e-3ee8-bdb9-79160ab5876e | -7.4097 | -42.09079 | 2025-09-14 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8486c818-48ee-3d59-9e8e-f4341cd34a47 | -8.63916 | -44.03731 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06e98e82-2706-3a0b-bb09-2e17918a026f | -8.50396 | -44.73055 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fdf98e2-776e-398a-a04f-2f7bbab59fd5 | -3.08307 | -49.46682 | 2025-09-14 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e57cb11-5fb5-3318-b5ea-5ccbc4b7b654 | -8.61896 | -40.1974 | 2025-09-14 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 878e0b58-454f-3e78-98e3-049a41c17aa0 | -3.79251 | -47.58517 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
