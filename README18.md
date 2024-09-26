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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87350c7e-36e4-3825-aa1a-c6fce3c155f3 | -19.1425 | -57.4617 | 2024-09-26 00:53:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c4235188-f878-3dbd-b54d-07768a506d2a | -19.120501 | -57.452 | 2024-09-26 00:53:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf7d8f4a-c504-3747-9e57-40be8d25dd62 | -19.113199 | -57.467499 | 2024-09-26 00:53:56 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3a413110-47e1-3843-b444-44a22aa89fd8 | -16.3207 | -45.661499 | 2024-09-26 00:53:59 | METOP-B | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5d159f1a-db44-3229-abbe-60479d4e7136 | -16.5495 | -46.926899 | 2024-09-26 00:54:01 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31048dbb-c713-3dd2-9a04-b1e78ae41a2a | -16.503 | -46.991299 | 2024-09-26 00:54:02 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9252e880-7e33-355b-994d-fb03380b48e0 | -16.5054 | -47.001099 | 2024-09-26 00:54:02 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d138138-ec66-3b91-969e-7b429eb74b17 | -15.9036 | -44.9916 | 2024-09-26 00:54:03 | METOP-B | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25bfeb4d-24b2-3e2b-a868-30f334275bf1 | -17.9146 | -53.652802 | 2024-09-26 00:54:03 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0b2303-3995-3c10-9333-fb1fdee55a33 | -17.9163 | -53.6609 | 2024-09-26 00:54:03 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed29a90-43ec-3b76-b885-0c133120bd14 | -17.9179 | -53.668999 | 2024-09-26 00:54:03 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5bef440-dba5-322e-9588-768dcd55dbec | -17.9065 | -53.663101 | 2024-09-26 00:54:03 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 902159b0-b0cc-33c0-99f7-434819ea8dc1 | -17.9081 | -53.6712 | 2024-09-26 00:54:03 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b663ea7a-0ea3-3038-9c55-e82adb29e68e | -16.3589 | -47.7253 | 2024-09-26 00:54:07 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b6ea799c-9e9e-3776-879e-2450cce4a419 | -16.342699 | -47.700802 | 2024-09-26 00:54:07 | METOP-B | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 841a8e2c-2e87-3d57-ae05-dbd1a24e76a6 | -16.68 | -49.135201 | 2024-09-26 00:54:07 | METOP-B | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fff6c778-71ca-33d5-8dea-d503223ad5b1 | -16.4562 | -49.016602 | 2024-09-26 00:54:10 | METOP-B | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76da1b4f-bdc2-34f9-84c4-f15076ad281b | -16.458 | -49.024502 | 2024-09-26 00:54:10 | METOP-B | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de832b3f-4dbb-3fa8-ae58-21a29f2f8b0f | -15.9992 | -48.126099 | 2024-09-26 00:54:14 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 39c59f00-b432-3e39-93c4-e0449dd5dca0 | -16.0012 | -48.134701 | 2024-09-26 00:54:14 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dfb1213c-89e7-3c05-a7af-4ab80017078b | -16.0033 | -48.143398 | 2024-09-26 00:54:14 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dd43a52a-817c-31c5-8e73-6fcb7ff955f2 | -16.005301 | -48.152 | 2024-09-26 00:54:14 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 9b89024c-8909-3e68-886a-bce106dd2d83 | -16.364401 | -49.919201 | 2024-09-26 00:54:15 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f8cbbdfa-2bda-3a88-92e1-6791eaa93452 | -16.365999 | -49.926601 | 2024-09-26 00:54:15 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5baa2cb-2771-3b7e-818c-c2f2b55ba5ac | -16.3529 | -49.914101 | 2024-09-26 00:54:15 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3245357-39b7-39f4-9422-a22651b97514 | -16.354601 | -49.9216 | 2024-09-26 00:54:15 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d6767da0-955c-3939-8cba-5ec27ec73564 | -16.356199 | -49.929001 | 2024-09-26 00:54:15 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f35fe51-8163-3e2d-8ffc-45e64455d264 | -15.895 | -48.869202 | 2024-09-26 00:54:19 | METOP-B | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af98a193-8346-305f-a9be-e48369f9fcd8 | -15.5289 | -48.4981 | 2024-09-26 00:54:23 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27167c81-ac4b-3702-bdd7-1bdad5f9cff5 | -15.5309 | -48.5065 | 2024-09-26 00:54:23 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b00ecf2-e478-31ab-a127-67d887afb028 | -15.3206 | -47.450901 | 2024-09-26 00:54:23 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2cbb737-a97e-376a-8188-df60d24c50f6 | -15.3229 | -47.4604 | 2024-09-26 00:54:23 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1048a42-9b16-3a9c-b84a-c44671ae2aaa | -17.1483 | -56.247101 | 2024-09-26 00:54:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9325d1a-159f-38f1-8547-b93d8f89d704 | -17.124599 | -56.2299 | 2024-09-26 00:54:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adce24e7-8c68-32f8-ae2b-be920582ef3c | -17.1266 | -56.240501 | 2024-09-26 00:54:24 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8b8cf73-c4fe-3553-98c2-55d4c7d49f02 | -14.6625 | -45.449799 | 2024-09-26 00:54:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4150f7eb-e93a-3175-9882-693283988e36 | -14.6657 | -45.462601 | 2024-09-26 00:54:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 193764e4-d8af-34c9-9346-a7f4b886d791 | -14.6561 | -45.465199 | 2024-09-26 00:54:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29194ce2-45ab-3a60-92bc-9fc44c9a2c52 | -17.114799 | -56.231998 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68d2fe55-b3a7-32f9-8277-d9305c16ea4f | -17.1569 | -56.4478 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc4662a2-e686-391e-b0ff-dfe59afddeb4 | -17.159 | -56.458801 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 207be00c-3b44-3255-abe9-f48e4e02da50 | -17.0905 | -56.16 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51a376ce-2261-34dd-9021-61c32ca1f6d8 | -17.0926 | -56.170502 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e22f0668-5557-3288-91d9-779e09b91146 | -17.0947 | -56.181 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd946a38-25a7-332d-8483-d225ade615db | -17.0788 | -56.151501 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d57eb33-0315-33e9-9873-4b334cb48d85 | -17.080799 | -56.161999 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43089008-8cac-3562-83aa-abdf67060b95 | -17.082899 | -56.1726 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98a9be99-2582-3b56-b13d-f6b7878e72a2 | -17.0849 | -56.183102 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aaa6467c-2133-3ece-ae5c-20f8ce1dad0c | -17.087 | -56.1936 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccc0e75d-8244-3993-b7f3-20cca3d7130e | -17.069 | -56.1535 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 462be057-c0c6-3679-ba31-ae8e028fb69f | -17.070999 | -56.164001 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce6c6d97-483b-309a-b598-c5401944311b | -17.073099 | -56.174599 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93bb727c-faf0-3e88-a256-7291f921375e | -17.0751 | -56.185101 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 442a00f0-1419-317d-be5b-b6e74b098915 | -17.0772 | -56.195599 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46022b5a-e100-3b66-a15a-3d06399161f2 | -17.0793 | -56.2062 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68428544-1c43-3599-8bd6-8d1d931a5c35 | -17.1042 | -56.334301 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84fafe82-7bf4-332d-9558-75126a17c5bf | -17.0592 | -56.155602 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 429db3db-4daa-372a-8d48-c40fa524a152 | -17.061199 | -56.1661 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d8d2ef3-2645-3fa3-b783-a519a988a0ac | -17.063299 | -56.176701 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb99c533-30e3-375b-b960-4d659f2ffd26 | -17.0653 | -56.187199 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed21e604-b5ba-3859-8250-5695b1608540 | -17.0923 | -56.3256 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccfdbb11-f851-3056-bd74-35523dd530f9 | -17.0944 | -56.336399 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1af3fdeb-0124-3dc2-9496-b14eda915e1f | -17.0965 | -56.347198 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e939208-4f52-3e4b-be57-4b153c3b0fec | -17.0494 | -56.1576 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 182ac3a2-0c2b-3374-bc8e-020af9983762 | -17.051399 | -56.168098 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16f79222-34fe-3236-b2fb-850993c66b2c | -17.053499 | -56.178699 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e602c139-d0a8-385b-8c4c-5e09babeb6f2 | -17.055599 | -56.189201 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b82be04-6770-3c39-b356-fa70436ca0d0 | -17.0868 | -56.349201 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5470f7fe-243e-39da-8bb6-31e2f8240312 | -17.0889 | -56.360001 | 2024-09-26 00:54:25 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af7bff24-3cca-386e-8c24-5f813e7888c1 | -16.619699 | -54.0751 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ee891cf-9bf9-3ec1-b391-cf661d497eaa | -16.621401 | -54.083199 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1664993-b303-320a-bad3-91afbc299a9f | -17.0396 | -56.159698 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 276f6131-3ae5-3bdf-8886-ec703ef0af87 | -17.041599 | -56.1702 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12d76dbd-a743-308d-b9dd-07d740590c1c | -17.043699 | -56.180698 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9cf65a84-9771-3ee0-9890-3651e3e68cda | -17.045799 | -56.1912 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac217a5a-58fd-3759-b043-f89b80954372 | -17.0478 | -56.201801 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 489da2b2-0ca4-361a-81cb-06d0fb71f27c | -16.611601 | -54.0854 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2aabaa91-f542-3764-8989-2510db7e3a33 | -17.0299 | -56.161701 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fcab03d1-b5e8-3849-a720-a4b05b8b02d0 | -17.0319 | -56.172199 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a08e6378-d00e-37e2-800d-f865db5cc81f | -17.034 | -56.182701 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3119fc3-81f0-3c48-a8ac-3553ca2d2415 | -16.6001 | -54.079399 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5507eaa-4b8b-3e85-bb1a-cab8898a1699 | -16.601801 | -54.087502 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7919ca09-09ae-32c9-b515-01c7602695be | -16.6035 | -54.0956 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4403ce69-4116-31d5-90ea-394b55e4c6e4 | -17.0242 | -56.184799 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb661d1a-6983-31d9-8cbf-ac661112a6a6 | -16.5903 | -54.0816 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8055eab-cdc3-34b7-a9dd-1b05b371eaf4 | -16.591999 | -54.089699 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40f126cc-c9a2-39d6-a2ae-da538896dd0d | -16.5937 | -54.097801 | 2024-09-26 00:54:26 | METOP-B | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5d2457-35da-3893-bb84-350a430a53bb | -17.0144 | -56.186798 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0eb141bb-7bef-3d30-8bc0-f2b7f561844f | -17.051901 | -56.378899 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3899c3c-1b29-38cd-9add-3d22e0d21d5f | -17.054001 | -56.389702 | 2024-09-26 00:54:26 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67d3589a-fb87-3ae7-9a40-2293668e8720 | -16.1057 | -51.994499 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 74b2091d-03a3-3f90-8141-909413b56604 | -16.107201 | -52.001701 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 17f0dc22-921c-3806-a300-3587afa7048e | -16.108801 | -52.008801 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c79ba7f-b9f3-3968-a334-20f4e6675c48 | -16.092699 | -51.982498 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73759807-5bc3-3f6d-9062-05bb326f1f09 | -16.094299 | -51.989601 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 05be35d0-34ff-3ed5-b957-dde39d4edb1c | -16.0959 | -51.996799 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9ca79a-d44d-3f9a-b83b-5ee23971beee | -16.097401 | -52.003899 | 2024-09-26 00:54:27 | METOP-B | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 932bfd55-7b90-39e1-bac8-048d0a93ecf8 | -16.983 | -56.1824 | 2024-09-26 00:54:27 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a1f9dfd-92c0-3e8a-a4b5-bb20e5ee44ef | -14.5482 | -45.695599 | 2024-09-26 00:54:28 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebdec72b-22a5-3686-898d-be07c266da4e | -14.4411 | -45.186699 | 2024-09-26 00:54:28 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
