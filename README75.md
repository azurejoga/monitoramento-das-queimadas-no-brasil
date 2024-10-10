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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd42ca4f-7a83-3a39-a1ad-c37f36cfafe0 | -12.34719 | -47.67448 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0584f34-339b-3dcd-92d5-a33ca681de7b | -12.28594 | -47.64549 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08d4597e-2d20-325f-9ed2-5510fa0fcebb | -12.28314 | -47.64116 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce07f659-29aa-335e-84ce-5b44e76ce1c6 | -12.28253 | -47.64491 | 2024-10-10 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 553e2b04-1f06-3172-a5da-8ed10100a884 | -2.1882 | -46.09506 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a01381-0589-3b95-a7dd-011270c97cef | -2.1853 | -46.09061 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 927c16cd-de9f-3a5d-906f-64db7057167e | -2.18484 | -46.0706 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e0fba46-64db-313b-a25a-3d7ebdf40206 | -2.18469 | -46.09451 | 2024-10-10 04:19:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82841da3-71a8-32c1-9cb8-b1d6fdccc2e1 | -2.18132 | -46.07006 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f98aaea3-39c3-3743-8e6b-7610408ce274 | -2.16936 | -45.94121 | 2024-10-10 04:19:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| dccfdd43-09da-350a-837b-1288c3d65557 | -2.16586 | -45.94067 | 2024-10-10 04:19:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f0f8088-3e89-3936-a017-febbf54f26b1 | -2.16298 | -45.93628 | 2024-10-10 04:19:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f16fe83c-88e0-35c2-bd1e-0417d1cd9f2b | -1.41124 | -46.44284 | 2024-10-10 04:19:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1c7f493-cdf2-3afc-a57a-7fe04bf20a9c | -1.3598 | -46.64765 | 2024-10-10 04:19:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5da4e7da-a898-30d8-9f71-2ae0607dd5c0 | -1.26432 | -46.35438 | 2024-10-10 04:19:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f42781fa-633b-3b81-ae26-eff3909f4cd7 | -1.26073 | -46.35381 | 2024-10-10 04:19:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e673fe02-dbdf-32e2-9809-d0a81962f169 | -2.40921 | -46.75343 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1221b8b9-7691-3d4c-b1c3-300a751ea6ab | -2.39405 | -46.70851 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c53412-8778-329b-be3b-cba55e0da419 | -2.39044 | -46.70793 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1fac72e-5b3a-38f9-b649-c35735ddf9fd | -2.36623 | -46.49057 | 2024-10-10 04:19:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a137958-1bd6-32f3-aece-e8487c6722b1 | -2.36265 | -46.49004 | 2024-10-10 04:19:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10bee993-80a1-37eb-9807-3be306498e1d | -2.34685 | -46.84182 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8156c6f7-b6e5-3a73-a049-87e3f7a5ff08 | -2.34322 | -46.84122 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c0da3d6-219d-3c02-8018-50f9c8fb3996 | -2.33664 | -46.45766 | 2024-10-10 04:19:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4559106f-ac20-3326-b905-4919dc983fb1 | -2.33307 | -46.45709 | 2024-10-10 04:19:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3f5ec93-31b5-39d4-8126-fdf857efb68c | -2.31056 | -46.55316 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a73023b3-eb0c-3566-a4c6-775982fe2a1e | -2.29223 | -46.97212 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2b2457a3-733c-38b3-9d94-cf5bcbd2c48a | -2.29154 | -46.9764 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 217ed14e-a397-33a4-ad6f-352c2a0bbe93 | -2.24242 | -46.74919 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63875f0d-fe7a-305e-85b5-044cd0878aba | -2.24146 | -46.73198 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b5f4e6-ace0-3c5c-a3e3-1620046c0b6f | -2.24013 | -46.74027 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94385900-0f3e-3f9d-8445-0f696ca84643 | -2.23946 | -46.74444 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfafee5-fb11-3897-b76d-1e0efc1df468 | -2.23783 | -46.7314 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b998df8d-3ff5-3fb3-8820-c0eab7d11e3b | -2.23717 | -46.73555 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11de8ede-96ec-3834-9e23-495367084dac | -2.20253 | -46.74292 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6319b8-239f-3fd3-95c4-c0d1bc28b1d1 | -2.20185 | -46.7471 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c88f474-081e-31c3-a25d-144600e313c0 | -2.20174 | -46.74424 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 398c5394-d5b1-34f0-bc72-df478b3be612 | -2.1989 | -46.74234 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84150b8f-8b5a-38ae-91da-3017921efc70 | -2.19876 | -46.73949 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f0d1127-5f99-3291-b454-53e7c11b2d31 | -2.19811 | -46.74366 | 2024-10-10 04:19:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec504e0e-1f83-3526-8d92-a27adf995bd5 | -2.60394 | -46.18113 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d511c4d5-71f9-3863-8b44-e540515d38d3 | -2.58795 | -46.12283 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a241f75-08b0-321b-b905-0fad5eee8fba | -2.54026 | -46.15105 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 319d09f0-8219-36c1-b901-238e2eeb3278 | -2.53674 | -46.15052 | 2024-10-10 04:19:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ff96ad4-1c0c-32ba-8e98-c84759bb2a7d | -6.54135 | -47.11643 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f464e19d-4126-3f6f-8d17-9fff39e69936 | -6.53783 | -47.11588 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 845bcafb-cc00-3119-9fce-1ee840006330 | -6.53431 | -47.11529 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21e0c312-1edf-3894-8974-7e9a3911f533 | -7.24062 | -47.49821 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1537756-e8b4-32ae-89a6-0370a57e6b5f | -7.13907 | -47.82574 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cd76101-6e45-3adf-b710-387c601d28d9 | -7.13773 | -47.83384 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7abb2cc3-73a6-3e87-b623-dd6e43496e18 | -7.13761 | -47.74509 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34d29874-bdcd-3923-b4d4-da754e779c35 | -7.13476 | -47.82932 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb216326-66b0-3aef-b489-7c00668841ae | -7.13408 | -47.83342 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 063ed728-960b-37f8-b5cb-7052ab56b2ca | -7.13333 | -47.7486 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9ee307b-0cb6-359f-99b4-769dfb58b1b7 | -7.13111 | -47.82894 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb4af79f-d6bf-3236-8a70-c5dbf4df4a56 | -7.10325 | -47.83848 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da586a48-5fb4-3a46-bb81-6d01920e0f3b | -7.09262 | -47.85819 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6cc8a2d2-3e8a-3ea1-be45-fa9a9ed6c098 | -7.08989 | -47.87509 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d0c000d-1c47-36d8-97c2-ea0cbbd91f3f | -7.08696 | -47.87016 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db760bd5-ef95-316f-bb9c-1f77022a6ad0 | -7.08628 | -47.87438 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e50e7afb-dcf6-3629-9153-6ed4ff675ffb | -7.029 | -47.37857 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06a4a07-01eb-3506-8a02-120e89136524 | -7.02676 | -47.37003 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 237143b1-6704-375c-b3e2-4489ecfe6407 | -7.0261 | -47.37405 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17184c4c-ed18-37d8-91ed-49c0e8734a1b | -7.02544 | -47.3781 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b1be389-0fa4-3679-a9b9-d89d30503af6 | -7.02478 | -47.38217 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96eccaf5-643e-3855-a914-0da3e8b5671b | -7.0237 | -47.21132 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93a18071-4d4d-302e-b0a3-6869edf92eb7 | -7.0232 | -47.36956 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28ef5208-d2bf-3ae3-b7b2-650ba62b1099 | -7.0203 | -47.36505 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac96334-acf8-32aa-8c84-30fd23573a2d | -7.01251 | -47.21346 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11202db8-ba3a-3141-9572-2cc4834333f1 | -7.01156 | -47.1973 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 654e68ea-1fc0-37f8-87f0-49afa99f0a6b | -7.01092 | -47.20119 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5d07604-c09c-3296-8e16-5b5f9b957b57 | -7.00925 | -47.2333 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6374affb-8806-3700-9dd3-58b69a8af32d | -7.00899 | -47.21292 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4675bc0-b6b3-301e-b126-a57efa54e4a9 | -7.00833 | -47.2169 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19da5f47-4c19-3121-a443-16ec4027e037 | -7.00739 | -47.20065 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7628c8d6-9e1c-3ad9-8884-13cf7f6eee0e | -7.00638 | -47.22877 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7da461f6-5f20-3d6a-990e-387376d0eb08 | -7.00572 | -47.23274 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 680e9a69-51d2-3207-a7df-e3212abce29a | -7.0035 | -47.22431 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5080b1d6-b3e1-322d-95bd-62c5b0ae055b | -7.00285 | -47.22823 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 928a20ca-3a38-3583-84bc-54a5d3aff1c1 | -6.99932 | -47.2277 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d91387c-a991-313c-aa79-057c0be2099f | -6.98575 | -47.376 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b67f7f6-d3b4-3c71-aa8d-d435b0fbe20d | -6.9851 | -47.37995 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47f08ff6-314e-35ae-8209-b032aec03626 | -6.98379 | -47.38792 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b47fc143-a7e9-3844-963c-d35af3ccf320 | -6.98247 | -47.39591 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0380628e-38b0-3c1c-bce8-828bb25907e6 | -6.98219 | -47.37548 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c381c30-0932-379e-8cd1-1bd766948ba7 | -6.98181 | -47.39993 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67fe50c7-d69a-3dfb-b783-ac89b93d0503 | -6.98154 | -47.37945 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cca47896-e527-37bb-8bbb-349359273ef4 | -6.98022 | -47.38745 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c78652-ba2c-3531-ae47-131bffa53df8 | -6.97798 | -47.37893 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e57d7ea-df7c-3860-b2d7-566f5acbe560 | -6.97732 | -47.38292 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7799c97-d76b-3ec0-875c-3e2faa32596b | -6.97667 | -47.3869 | 2024-10-10 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b56e8693-1c65-3617-83a2-7c169b694df7 | -6.93087 | -47.73039 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ac8455d-1e97-39ac-919e-55200062aac7 | -6.92864 | -47.7215 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84b04ee0-2189-3beb-a2e1-b664b2b2df9f | -6.92795 | -47.72564 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0fa6a80-970e-35d8-b846-d6f438353f07 | -6.92726 | -47.72978 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43519e8a-3871-371c-bb1e-afb032970717 | -6.92637 | -47.7128 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f8061ace-a171-3f55-bbdb-a6094d734a56 | -6.9257 | -47.71685 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c331566f-d804-3ba1-8c1f-067129442b93 | -6.92503 | -47.72091 | 2024-10-10 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a53b52c9-9c83-3b41-9b07-2bcd1cb7af95 | -6.85807 | -47.3444 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ef1bb63-faa0-36ee-b0ab-7c4655ced0de | -6.85516 | -47.33987 | 2024-10-10 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README76.md)
