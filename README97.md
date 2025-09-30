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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c80907-9c8c-309f-9d37-a209427ac4a2 | -15.28984 | -56.78929 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76701106-b947-39c2-8346-7f0bcfcedf65 | -15.54338 | -47.86792 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddce676b-3fe8-3e4b-a1d0-bf82ddf1deba | -13.82199 | -47.49577 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a6d9dffe-07cf-3d56-bbe0-b746ee393c9c | -17.89412 | -57.60306 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| deaa6dda-63c6-3019-859f-0f80e8b715a4 | -14.68949 | -48.13733 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be09f685-6736-3371-abca-7d26bbd70092 | -15.27304 | -47.85286 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68d39523-a376-39fc-926d-30b0597816be | -16.06086 | -51.02919 | 2025-09-30 05:10:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa63d19-9e3d-3207-a5cd-afd395cd89cc | -20.62215 | -46.18051 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e99028a6-f0d8-3fd9-b5d4-8130fcb4bbd3 | -13.81185 | -47.48458 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28a37242-d089-37fb-9f3e-1ddae1db07e3 | -13.736 | -54.72044 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e960d35-f225-33e1-b3ae-48117fd3718f | -15.27586 | -48.02631 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef55b817-ac93-395c-a286-221a6d93a0c8 | -15.29536 | -46.41053 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0738b631-dc8d-3224-b0eb-c70716c60eb3 | -13.76094 | -47.92236 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d9c37c6-7876-3b13-b75b-8ecbc9f2e146 | -17.39744 | -47.14365 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| add1d80f-ab31-3ac9-994e-37f39e202365 | -15.29265 | -56.79345 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4615ac90-a5ae-3617-b164-277279036c09 | -14.51409 | -48.45393 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5e2e0fa-04b2-3428-a98d-845b98de5d6f | -15.28037 | -47.88835 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2b27494-b0dd-3666-9268-8215d357a295 | -17.88686 | -57.62796 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f9d30f77-9a84-3f66-96be-c9582c7e6a00 | -14.51046 | -48.46067 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6e54e16-941d-34fb-bfa5-1079bd792a54 | -13.76245 | -48.322 | 2025-09-30 05:10:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e76de7a-b8a5-31b6-a87e-26db78d71049 | -14.58866 | -48.28071 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4606475c-75d6-3094-b785-cdbecc606c2e | -15.72361 | -59.50834 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79f53700-535a-38b4-a88b-1ba4c8adb34d | -14.71547 | -48.24643 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee934bcb-5d4e-3b58-93fe-177a5df79169 | -13.80454 | -47.97558 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 503a3dd3-9baf-3518-802e-918ccaf41c3b | -14.59327 | -48.28811 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f892872f-24b2-3e85-95fb-35702db4c737 | -14.79232 | -48.30402 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b938ace-8bee-3c9b-aa7f-7220659366c9 | -13.03229 | -56.90073 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f7af8fa-7b2e-3d9c-8a93-07eef0072c44 | -13.79023 | -47.9563 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf1197dc-e800-3a7c-b416-042811ac6c69 | -13.8382 | -47.50373 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9b395b8-b9fb-3f04-b519-532eed1936be | -14.52558 | -48.4482 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c80f71e9-3c3a-34a3-ad51-94116e1fadb9 | -15.84485 | -59.59895 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2972f601-cf67-341e-ac93-714ff28fd0c9 | -14.53931 | -48.23256 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbe932e6-e4f9-3d82-8253-693d2c1e3a22 | -15.93307 | -48.12675 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dd72132-246e-3777-8672-343d785d0af5 | -15.4889 | -48.55718 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 653620aa-5bac-3427-8cc6-281e1e222185 | -15.80164 | -59.52151 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f59f52b3-abf1-37ab-a8dd-0913a8f1e6fd | -15.71842 | -47.59808 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0139bc66-344d-36fe-b598-9f4d3f5b77d2 | -14.53136 | -48.24304 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc9c8d0a-6b4f-3626-9ffb-1eab329c55d6 | -21.04782 | -45.68857 | 2025-09-30 05:10:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88e53ac3-498b-3601-89cb-0c6faca6e6ac | -15.70361 | -59.48135 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77ae8997-a402-301a-88a3-4b8a1e54782d | -13.78488 | -47.95465 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5840c9a5-007f-3e0c-a4f3-0959400689b3 | -15.4232 | -48.24773 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99b57799-38f0-3e92-8231-04a8e70152c7 | -14.70401 | -48.25027 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a802448b-1968-357f-aee4-5d574f6f3cc6 | -13.81173 | -47.96196 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22ea2470-9f01-386f-9901-d2eaa2544a52 | -14.68556 | -48.17154 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae31ddab-3e0d-355b-9716-8371a0b3db4e | -14.55194 | -48.26622 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84f42e46-2aef-3345-a0da-2fbe73d899f5 | -14.52389 | -48.48363 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d6bd953-9377-3ba8-8e76-c1cccabd284e | -15.37687 | -47.0802 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cdf2e8c-d524-3841-b526-c3bbdfdaba55 | -15.26728 | -49.26465 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9a2594b-38c5-3a13-9036-3ed563213921 | -15.33833 | -47.82948 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93796d62-bc5e-3330-a7b5-947f37c04fd1 | -13.75258 | -54.73148 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5962e2a9-f86a-3e19-9610-2d11f9fe78ac | -15.92828 | -48.11947 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1859328-4c13-3597-93d4-b7927999cf80 | -19.85817 | -44.55809 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 07fd06cd-8395-312e-b297-fa6fa2f61fbd | -15.46541 | -47.92206 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceef06af-87ee-31b7-9e3c-6292e00fde40 | -15.26985 | -49.26192 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3587f107-7894-36f8-ad49-cea626d8c1d8 | -18.32975 | -57.10132 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 70872ee3-9fb0-3e5e-95b1-5c5ce2779628 | -14.53588 | -48.25109 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b033d56e-093c-3cae-a4db-4ffac4aa99fb | -13.8502 | -47.49886 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 922192e3-fa86-3aee-943c-ac1332346bae | -14.5523 | -48.2631 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40abd2c-2944-3049-b8cd-213d588f86c7 | -14.51939 | -48.43187 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85cc7439-a004-3734-8cf7-4616406de936 | -14.53341 | -48.38015 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 095e0cfb-3f0f-3519-a703-2359a0867e1d | -17.10256 | -48.57101 | 2025-09-30 05:10:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b92b58cf-6390-36b1-b94e-9b73a4f5e9e5 | -15.89321 | -57.4931 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fb1a651-52c5-359c-b599-307965a45553 | -13.03512 | -56.89787 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e03203d9-bea7-322c-9ab4-ccdbd82ef14c | -14.51493 | -48.4239 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81fb3163-4d86-32b4-ac53-5d618d441800 | -12.39642 | -57.58215 | 2025-09-30 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 280d92b9-dc76-38d2-a07f-445aa079be4c | -17.39028 | -47.15458 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f32bc00e-8005-37e0-974d-11707b987de5 | -14.53104 | -48.38099 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffe59ebe-f289-3c48-b7c6-27b9db2a6149 | -15.86347 | -59.33591 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e66d5f1a-81f6-3929-ab12-eb6624071ca4 | -15.90458 | -46.24739 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56bfbd6d-afb8-3ac8-b17b-db6bbebaef7e | -14.53714 | -48.24066 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| defdfb6c-4909-31cf-b497-7fbae2dbe6bf | -14.56663 | -48.46782 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0a78ddd-da75-3c18-a363-88016df27363 | -14.53881 | -48.38048 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 124378b7-36f9-38b9-a835-437ffea2acd3 | -15.5452 | -47.87042 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af3ae1e5-4504-3cbe-9db0-845776ff465e | -13.7885 | -47.97079 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e69ad206-9f2b-3e27-ad50-40ed80697874 | -17.3966 | -47.15216 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e44c97f-b00e-370b-ac3b-e56ad4b93bda | -18.48211 | -44.02571 | 2025-09-30 05:10:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2cb6746-7cc9-368d-b1b4-25c7e4521652 | -13.73411 | -48.68134 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e892eab5-ff57-38bf-9945-0172115f1b36 | -14.72991 | -45.22273 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77b3db36-bcae-383e-b182-8d78c35a8c2e | -13.76681 | -54.73371 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b60b9226-a82c-33a9-b087-2d2cfb3f138f | -13.74108 | -47.902 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 654a2a5c-d728-3e67-8530-3a67be05cec3 | -14.78508 | -48.31907 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50308240-c958-350b-9b04-220365e0444d | -15.92991 | -46.20738 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 73a70a6d-e981-3cd9-9fc2-fc2acfad0912 | -17.0975 | -48.5665 | 2025-09-30 05:10:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b73749f9-e8b9-3a92-9110-532a10aed50c | -13.73199 | -48.65594 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 391065e4-ec7f-366a-8b49-fe25d027ac01 | -14.54725 | -48.25932 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a24b7f6-8b1f-3843-84b6-42a037336011 | -14.54356 | -48.47994 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f368599d-c3e3-3e06-909c-da49115f18d7 | -14.79156 | -48.31059 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa67c8e2-38da-33cd-9dcb-9c937093f117 | -20.06685 | -46.79275 | 2025-09-30 05:10:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56a975c1-b449-3bd4-b1a3-4154ce025ff3 | -15.91959 | -46.24461 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c07a263-a59a-3415-ab25-d56ec2c5273c | -14.51404 | -48.43124 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5de77ae-14d5-363f-bf78-b114e9099290 | -15.71072 | -51.7835 | 2025-09-30 05:10:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 051b966a-66fe-38e2-b196-69f246e70eb7 | -17.91537 | -57.60952 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1e983c38-a2b3-30e3-bcd3-faa5659e6fcb | -15.71557 | -59.51476 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcd14db7-3a78-3b86-81b5-84f12411212a | -14.72992 | -45.66688 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae4d2681-0342-37ac-8a40-b2d17cf0202a | -15.91339 | -59.50195 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61728684-3278-3336-8433-dd556a80eb88 | -17.41331 | -47.1548 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa12436e-d4e1-3794-a9c6-834de19aba79 | -14.08839 | -44.09181 | 2025-09-30 05:10:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05016f82-8100-31b6-9c19-446a5e2e8d0e | -15.28339 | -47.86178 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd098869-e3fd-39bb-a2ea-4d02677c71ab | -14.59357 | -48.1916 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8379ffb1-7c14-369c-b1de-1bb02768d1cb | -13.8375 | -47.50964 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README98.md)
