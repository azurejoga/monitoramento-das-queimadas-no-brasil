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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a21b1281-f148-35a1-98bd-9b0237644dc1 | -11.80704 | -45.04903 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d296c5d-93e6-368c-a393-fb77d9f244c6 | -11.86981 | -56.88333 | 2025-10-07 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3301e223-8d2a-30f6-81b5-6fb16738671d | -14.94566 | -46.8211 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e2c6de2-1b4d-39d4-8ade-bb97b4f78714 | -17.61163 | -46.68803 | 2025-10-07 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a85a1c3d-e430-392f-b8bf-b9448d76feaf | -13.27075 | -47.57292 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bcccd61-e76b-3d47-9c72-d2dd7c7e03d0 | -15.61353 | -52.56305 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a302846-12b5-3656-b38f-fd34b1754a99 | -12.90977 | -54.7308 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52e01416-4f8e-3df8-b5d1-5213b4922e1f | -13.67735 | -47.33881 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 491268d5-e813-3336-a5e8-b09abea05c35 | -13.38849 | -47.57657 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fdec763-d7a8-3aa9-89d3-4db49af32ed8 | -10.62262 | -48.70135 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87a4d7ac-a50f-3f78-b509-fce6aafa9db9 | -13.27818 | -48.46442 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cce862ef-50b6-3185-8b55-6f4e512c3901 | -9.16922 | -59.55366 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bee49a0c-9791-3cc0-a768-92c79206d7af | -15.5875 | -52.54601 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0474f40f-aa99-3e91-9a2f-dfeb97776afb | -12.93969 | -54.72881 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eef9bd0-a7d5-3017-bc10-2834c659eda3 | -11.21237 | -54.98705 | 2025-10-07 04:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ad5f1ed-9f27-3d4d-a7c0-1492f80c6e5a | -11.64832 | -46.87422 | 2025-10-07 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc303853-7fb7-374c-a3a9-cb9a8862b26f | -17.71287 | -40.24904 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f379c58-2cea-30e7-b07f-5136be63121c | -13.65789 | -48.72782 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef7b35f9-325e-3212-9198-190225e280b8 | -15.59739 | -52.57299 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 48619817-9b94-36bd-8629-06661ff9b742 | -11.78335 | -45.13209 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ef962f3-f0a3-38cd-89e6-fb8a19f388e0 | -13.3662 | -47.2527 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e4943d4-b314-3eba-8c25-d4f12d88b202 | -14.6442 | -52.52906 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10e1afea-0218-3aec-a8bc-27810a552769 | -13.2681 | -48.46283 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1be73759-1fbf-372e-8045-8f3d8cf166b3 | -9.61728 | -57.20324 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37696c8c-ef0e-3734-87cf-5f5da13ac476 | -13.68561 | -47.95918 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9007d09c-e450-393a-89af-1b2652536203 | -13.07264 | -47.889 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b8c11db-0240-308e-b3b7-5fa9e87f3184 | -14.77385 | -46.05135 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 55e24a74-3184-3111-b71f-50552ad4e3e2 | -13.34809 | -47.17813 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74f9ad6a-baa0-30dc-9f22-340ecfa78396 | -13.85738 | -44.41588 | 2025-10-07 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c39411-0c0c-31b8-9b39-e25684a94d27 | -10.38199 | -50.30035 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0de5f3a8-f2e0-3b2b-bb86-ee430a789825 | -13.58787 | -48.14579 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e85ac5c-e265-36c8-a401-972e26b34e51 | -11.86403 | -56.88767 | 2025-10-07 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 61c5db41-295f-39a0-9e96-78c0fd5f84da | -11.94634 | -51.4698 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a196fbf9-efd8-3919-84f6-fbb4a36a7af1 | -14.64282 | -52.53722 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79eb0609-3654-3729-825e-54228f2fdfdf | -11.7764 | -45.12655 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 078797ed-1be9-3311-a63a-afd46ee5f8d9 | -12.89893 | -54.74404 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf4f7caa-31ef-3990-ad85-c693d6d7e725 | -14.76329 | -46.04509 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d7d293c-e317-355b-8dea-b82ed54912cd | -10.80106 | -48.59618 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a411cbfa-af6e-3d4c-8ec7-1b10a3ae26ad | -11.23191 | -48.69408 | 2025-10-07 04:38:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d766ba5-8651-3f14-88ff-53c1f6fd1100 | -10.3964 | -51.60226 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74906c29-674c-3b7f-bce9-80df47805a2f | -14.97006 | -49.95363 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1c48de3-a9de-3c75-87da-9b4576c143b2 | -17.34544 | -46.83561 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc457ec1-996d-326b-b8c8-f1341e61ee75 | -13.33481 | -47.55898 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27be49d6-2d8a-3bc8-94a9-51c9c8e58184 | -9.51662 | -54.73565 | 2025-10-07 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d736b2d-f530-3340-85ac-e7453b9e03e7 | -13.2484 | -48.0629 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1b46245-7118-3fa5-82ee-94e0ab95c0b9 | -14.91701 | -46.8155 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce7a6f43-206c-394f-afd5-2ee513b3d554 | -9.17156 | -59.55225 | 2025-10-07 04:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02ad1b23-2d40-3c4f-b604-d4c0d4d5da62 | -11.94585 | -46.45209 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 875df35e-34b6-3341-a7b1-629041849780 | -10.38478 | -50.30458 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea4572c-001c-3720-aa0b-d5ea39416e5b | -13.69014 | -47.95225 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52a81213-77d4-3fc0-9688-dd0d5926e6b7 | -13.26485 | -47.79208 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c5d25b2-6bb5-3ac4-bf43-c0314989fcca | -10.43214 | -50.39925 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e2400d-ad2b-3f93-9323-08e61f7ff550 | -13.05521 | -48.70908 | 2025-10-07 04:38:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8087682d-0dc6-34c3-bb1b-dda9d1a0258f | -16.0209 | -51.05208 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b88477b-94cc-3e34-ac3d-c66b945d2d0a | -15.96496 | -50.83714 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5716308-3616-3c0c-ad86-1d08764e3f58 | -12.2346 | -43.77848 | 2025-10-07 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5daa9efd-ac91-35e3-a5b9-6d8e9c428157 | -14.55359 | -46.62696 | 2025-10-07 04:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ab3cb13-4a2a-37db-ab7d-0bfebb88503e | -13.68903 | -47.95967 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fabb5f4-1a4f-31e5-88dd-80408eab6bfc | -12.41009 | -51.14137 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a092a46d-6806-3a83-8988-674f4f7cf268 | -15.26962 | -48.06197 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 753103f6-4044-3319-a932-2dbd73e9084b | -13.09315 | -48.00548 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 670874be-137f-3797-9b18-fa816f2cd8d2 | -12.01731 | -47.79041 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60d9ac3a-180e-35d6-845d-0fbae205af5d | -11.48802 | -44.97123 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5fef5ce-f063-33d1-bfb5-6dbba0fe78c7 | -13.23427 | -47.24831 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8880c909-79bd-3ee6-bd83-ae89da892831 | -11.94441 | -51.48133 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 995ba00b-dfd9-3167-98de-50eacce8e145 | -13.24347 | -47.23424 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56001dc8-a8a3-369c-b205-95caf6398265 | -13.27176 | -47.16327 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c35c21f-0af9-326f-895c-3f39e1de8ae3 | -17.08767 | -43.38255 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d89b7ed-1337-3062-b4ae-a5f3a5180f23 | -15.48252 | -47.94096 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b2fde26-e140-34a9-b609-76e5a471ca22 | -13.72475 | -48.20532 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba2d18f-1511-3ab0-aeae-1ab81b0a6397 | -15.98927 | -50.94209 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb43f0d5-81c3-349f-baa3-7df5379f5b65 | -17.56081 | -50.44184 | 2025-10-07 04:38:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e58e5c2-b988-36a1-83aa-71aee53a8d13 | -14.64488 | -52.52502 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8061cbce-49da-3d1b-a79b-16404440279c | -14.68771 | -48.38518 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be3eeeba-aa5d-317f-b312-dbeea115b626 | -12.16535 | -50.90796 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 566065fe-a895-3a03-8025-4647c3151ca1 | -14.77629 | -46.06103 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 315b8b1a-2823-35ad-9b49-3a668efafe21 | -9.6206 | -57.19864 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4f2e87d-7619-3d84-b81e-39a4b61809b3 | -12.89417 | -54.747 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d97454d3-fcee-3960-a378-8ec29c277d6c | -15.44035 | -49.0974 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0669d0-050b-331a-acb3-beef234bc673 | -11.81337 | -45.11233 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8378208-7bda-3c68-a18e-b9a5bd2c1495 | -11.78421 | -45.0993 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c31a2c7e-b02b-3304-9efa-993bac3d5a9d | -11.7726 | -45.12603 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b2709ef-bd94-3d24-996c-d69392b570d8 | -14.93013 | -46.80093 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 020ff761-35f2-3d3a-ae27-eca6c582d39c | -13.09426 | -47.9982 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17073eeb-8aa7-35b7-9de2-42c78dd6cf45 | -15.76058 | -47.77081 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5be2b965-7176-3292-b3c8-2ed45d2f30ab | -15.68543 | -53.62626 | 2025-10-07 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aff971e4-dee7-32ce-82c0-10e7f17ae437 | -15.59314 | -52.5554 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6794a037-52bb-3033-8df0-5bdf5382e2b9 | -15.63796 | -47.62298 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5e29477-582a-3076-82ee-5cf18503727a | -14.92091 | -46.80865 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7cbdcbe-051b-380c-b5e1-6a539c64eabd | -13.22567 | -48.45987 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41ae2c7d-7f76-3030-a995-e39d8920e076 | -16.29629 | -50.98708 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49105d84-8212-3e2e-8710-5dc71f2c2379 | -15.5583 | -52.44203 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4be5f598-2e5d-384b-9cab-d41bab2ed79d | -13.23796 | -47.23823 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd39f1cb-3f67-375c-96c4-90204b12316c | -13.72601 | -48.06073 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15d90993-fa36-3fa2-8683-8eaafac51261 | -12.98839 | -46.78896 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1564d18d-88c1-3757-87b5-e3b54d0b2f32 | -14.64576 | -48.34019 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4d44bff-23f7-3dfb-ad6b-9df0a5896a45 | -16.10742 | -48.94603 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3cf81d4-f98a-3b98-b79b-96e9207fcef1 | -14.7378 | -46.03634 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 19534b4a-d1db-3dad-ab9e-37f84c0daf1b | -17.26168 | -46.802 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d566ff3-11a9-3a06-8f57-7eba5f649ea8 | -14.73907 | -46.02728 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README77.md)
