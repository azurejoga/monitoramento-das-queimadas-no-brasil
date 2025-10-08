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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ade308f-6438-3d1e-8aa7-42d45ff03263 | -9.18023 | -46.91309 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fcdeea9-ec53-3ea7-be8a-d707b3a827d8 | -14.70745 | -46.08627 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f6a7276-8d09-3f0f-a237-6626016a8442 | -17.8298 | -57.62605 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3976293d-63e2-37ee-a6b0-77f53367b8a7 | -19.50995 | -44.07912 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 101efed6-0107-353f-9fff-d57b20333cad | -17.26955 | -58.12346 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 42e14f53-3df6-3ebc-a2e4-e886c27f4c80 | -14.92583 | -46.79651 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 583df5de-9a93-3bb3-9796-cd73014e9c34 | -14.52877 | -46.64069 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 416c22c2-15b6-3368-9e3f-3b29f874676c | -14.7012 | -46.01083 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34d5996e-bfe0-3232-839f-3b06c66508a4 | -15.36854 | -47.32323 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 904dc16d-16d7-3dea-8e97-792d2bd068b3 | -15.39974 | -48.0096 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7c095c2-fdb7-33ec-b683-61a8d3712ee2 | -20.40576 | -43.67125 | 2025-10-08 04:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c33a96f8-fdac-3ed1-839b-2d9fd54ba4b2 | -17.13003 | -43.46197 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 804fccc5-24d0-3343-a0da-551cab30c2a8 | -8.59993 | -48.2547 | 2025-10-08 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1206b4ea-6a35-32c3-854c-1b21ffb70413 | -14.82865 | -48.41671 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c613456-cb29-3c56-ae7b-44f9e819baae | -15.25953 | -46.34124 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2825d2f7-d8ed-3283-a9d6-a554da9cc88f | -7.79941 | -44.20977 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c83d5fbd-7aa0-34d5-866d-fe4944ff5a54 | -18.05102 | -57.54485 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79562a24-f7dc-3a6c-8441-b1012e0f0011 | -17.55376 | -46.06624 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20029f3d-cfc8-3ec5-ada1-244875a7121e | -17.28422 | -42.65496 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 159afbbc-aeb9-3289-9527-f14737862f06 | -8.27131 | -47.00843 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f10fddc7-cb8c-38ac-86e0-5571d0f8fc47 | -8.22759 | -44.17724 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0567d96-e2af-3c33-bd76-49db4289ae85 | -17.16584 | -56.60729 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 89811de7-bfff-36b4-bb02-ae37bd409d44 | -18.01788 | -44.94419 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 746ce83b-d312-3873-a4cb-27a9281d1872 | -7.7673 | -44.92968 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed79650d-2de5-37f2-8a15-e080904c9011 | -15.37543 | -47.32455 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 047a4e4e-7287-3269-af6a-235e865be4fe | -13.88592 | -51.91011 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7817d76-876d-3606-8f0b-ac9e5bb41954 | -8.55084 | -46.22945 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e3e450-1828-3d14-8741-a07f0d6a41cc | -13.38017 | -47.56695 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 216e7399-2e1c-300a-8ca1-593d5ad00823 | -19.81704 | -43.89484 | 2025-10-08 04:19:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f40981a0-22e2-35ca-aa5a-43526bc6015f | -13.80851 | -45.79031 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4eda4c9e-1666-378f-bd73-60242f0819a9 | -8.10764 | -44.77306 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f901065d-fce3-3260-9e89-e9dff71ab715 | -8.23201 | -44.19236 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 262071ff-d13e-3e01-b2fc-0156e12c0b2c | -8.11101 | -44.7736 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea26044c-e28c-39ca-bbb9-b44fcf1ceeee | -20.50043 | -45.94864 | 2025-10-08 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f84917a7-59ea-3bff-987e-e738fb826712 | -15.94743 | -42.60289 | 2025-10-08 04:19:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| bccd3604-7af5-3b04-854f-95980b2f9637 | -17.94454 | -57.5104 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f7760b9-ce76-3e20-94f5-99ff62bc8224 | -14.36232 | -45.23109 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4457fcca-d9b5-3163-ab11-d37d5654f73a | -17.35827 | -45.05822 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36c42578-1d05-3090-902b-97a1f42d7a21 | -15.35113 | -47.33332 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3536cd4-5974-3ebe-a1bc-a60f1cd199af | -10.08834 | -40.77753 | 2025-10-08 04:19:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90d06342-c8ce-3d5f-8dc8-307e60366743 | -15.0738 | -46.62111 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5f89318-91c8-3c77-931a-6112b5ced9a2 | -18.50776 | -43.89624 | 2025-10-08 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb42dfbf-5328-3e34-b7d8-ecc02264b3da | -17.93851 | -57.5106 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d2541f27-3bce-3da0-995b-48e90f2f27d2 | -8.15866 | -43.33196 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e624db56-f4f9-3902-ac0a-2f633f223c9c | -13.72637 | -45.66927 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be4ca30-d330-34de-959f-78787e8cd8f1 | -21.30123 | -45.95088 | 2025-10-08 04:19:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2e9a575-5ac2-35f4-ab86-2d879361698e | -17.83232 | -57.64388 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| ccacd26b-c50d-3a8e-a62b-87d3f9d30b5b | -8.62313 | -45.10397 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e588b9e2-9730-3d42-b0f2-1b4660446186 | -8.52388 | -46.2826 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76dd19b0-43db-3f78-b752-d4688bdd9527 | -8.47765 | -46.27998 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 84a61cfc-3727-3378-b3d2-7645ba6de309 | -8.17521 | -50.16348 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1582aab-9838-3348-89db-600aeecdebd0 | -8.5997 | -48.25159 | 2025-10-08 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ea11135-b18d-3d4c-84d9-08c4065fe65a | -17.81739 | -45.32082 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cba64e6-efb2-3729-ac73-35c8e207a422 | -15.60922 | -52.58221 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c48a15d2-7d2a-3dd3-9fa0-7906fda35e95 | -15.25652 | -46.35973 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a042a31e-3f76-3e6b-85f8-a9ea6b871367 | -17.82969 | -57.62722 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| de6417e3-57f9-31f5-8953-ec7d93f40a38 | -15.42506 | -43.05413 | 2025-10-08 04:19:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46960559-31f7-3cbc-bac2-b4eb456e83fb | -9.3975 | -45.95042 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e142c46f-0771-36c6-841c-346421e834fe | -9.17953 | -46.91726 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c0a87cf-6367-3af5-8c6b-1e2f3a873fc6 | -17.29073 | -42.64557 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3d66b70-8d98-3075-9469-b22c48c0f2f3 | -7.78435 | -44.21819 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59953626-5748-369a-91a9-0b084c401e37 | -18.49968 | -43.903 | 2025-10-08 04:19:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55a25e9a-b8b1-371d-afcc-950adfb93217 | -17.95697 | -42.94336 | 2025-10-08 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d4fcd9f-e884-3fdd-a171-daed79da3c70 | -7.79474 | -46.01792 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cbc0bed-883a-366e-8ebd-44ac833a0c8b | -8.40989 | -46.80728 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 661e4b30-ab8a-3d71-a016-e89b492b9571 | -18.06988 | -44.44489 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e42eaa-361e-3d46-8a63-696990e60608 | -19.59932 | -44.65198 | 2025-10-08 04:19:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 468a2196-6533-383c-b9d4-7a374a84edba | -8.61974 | -45.10343 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 592de689-eed5-3af6-927c-281590ec02fb | -8.53959 | -46.23174 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a23dd931-1143-355e-b2f3-3dffdba24a9f | -8.60954 | -44.90549 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54d0246e-37da-3feb-9a96-3d65f1e3b0fd | -9.18384 | -46.91373 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44a59fda-8199-3787-ad50-1440ea644bd0 | -8.22924 | -44.18832 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa5009a-e5e4-36af-bbc1-da7f453f60b3 | -14.89897 | -48.0908 | 2025-10-08 04:19:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7af2c9cc-2288-3209-88fc-e93e190b9a15 | -15.77333 | -46.25543 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69684df6-c8c7-3842-af91-3f42785d8ab9 | -17.92671 | -44.60987 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33fd1063-6319-3b2c-bd6e-8e9256e95090 | -15.66679 | -43.65572 | 2025-10-08 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90f0f99b-92a4-3d30-983f-885c799b1f4a | -14.3877 | -46.02508 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e5aab38-a2a5-3c47-915f-e6c3436e86dd | -8.23145 | -44.19588 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 34f83839-1a58-3956-a647-889dff979921 | -20.20391 | -43.95151 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 9a0cd99a-e3a7-3a3a-83d8-8fad3baa4f9f | -14.70849 | -46.00836 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6844dcde-09db-398c-9d28-2d626575743a | -9.39529 | -45.94216 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad1799a8-0f5c-3479-951a-83c1de5701d4 | -8.4106 | -46.80294 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbc7694d-7a51-3e8e-bc16-f04cf8777d82 | -19.81976 | -43.08366 | 2025-10-08 04:19:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 65eb87b2-804b-33ff-80a4-287606465cd9 | -9.17442 | -47.81818 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 616923e7-f4e6-3f13-99f2-7d0490927197 | -9.20826 | -47.84054 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f5dbb8d-99f5-34d1-94c2-b324037d07d5 | -8.18194 | -43.33564 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0eb7664-c90a-3ae5-9109-dc2aee57fe66 | -14.94636 | -46.7996 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8908d62-7325-3959-baef-8ec8b455b98b | -15.37359 | -47.30497 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cf946b3-2ba4-39df-a47b-742041bb54d2 | -13.38617 | -47.60767 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8c32ef9-d0bf-3eb9-8110-8f1b352117b9 | -14.62232 | -48.13757 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ded4bc22-d07e-3406-af97-eb384e34a7fa | -21.15894 | -45.62628 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da95a643-6193-3712-80b5-0b11e553ac55 | -19.83206 | -46.16042 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcd9da31-4dc6-3e8b-993d-9aced1d55c65 | -8.37137 | -47.75963 | 2025-10-08 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 422092db-21a0-382a-a1f6-9ede2842a6ab | -13.7549 | -45.74812 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8528a8c4-5365-3687-86a2-b8dcb61d8827 | -20.08545 | -42.7111 | 2025-10-08 04:19:00 | NPP-375D | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a78482a5-056f-31d8-8db9-f354c6e76c0a | -14.79422 | -41.63275 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba98d2d1-a742-3d6e-988b-82bc6889bf7d | -17.93858 | -57.53827 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3968f1ae-58c7-368c-8d77-66e90e9a0553 | -8.56472 | -44.62629 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21be1c5c-6680-36d4-8ac6-9fcb4ea770c5 | -15.38453 | -46.27961 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 349f266e-7995-3be2-8947-05844b031f9c | -15.80527 | -46.24966 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
