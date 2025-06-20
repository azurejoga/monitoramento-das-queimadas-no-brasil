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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f2928a-a2c3-3aa5-a77d-ef98f9167be7 | -10.6651 | -56.55251 | 2025-06-20 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 89dc3ca5-69a1-37a4-a61c-908dba175804 | -11.13238 | -46.67313 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ecf7172-2216-30bc-a66e-20c66a177825 | -10.82926 | -54.01603 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ca64f85-7766-39df-9a39-c2e67e8a5219 | -14.81435 | -48.46458 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e30f47-000b-317e-9ffd-68934cff1cb2 | -9.49122 | -56.08702 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b08c135-6991-32c9-ba0d-a919f5f05708 | -13.29147 | -57.07321 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc2fd7f-dfea-3951-a871-3ef6b3e7930a | -13.39301 | -48.4509 | 2025-06-20 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc89df2-3a9a-3acd-b0a2-693f6df63d9e | -10.53048 | -46.64487 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f72b8046-18d3-341a-a05a-cf1b8fc9c36e | -9.45351 | -57.84142 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45d50af7-b11f-3ef5-a2c1-b37a5107f4b6 | -9.3301 | -47.83379 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f81f1be9-b922-3c86-98c5-c566d30aa046 | -9.48508 | -56.07706 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d0aa5083-f47b-3bd1-a4a7-89e7b524edda | -10.86018 | -53.76486 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d7b5cf7-9ffc-38f1-9fd6-4f67579245c7 | -10.46847 | -47.04864 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 07991de0-af0a-3e17-8540-e71988168f2f | -11.94501 | -58.74214 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 35c275a6-7728-397c-9c6f-d5755f4b5ea4 | -11.95406 | -58.75116 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e32eb93-3704-38f4-858c-e94493674efb | -10.54677 | -46.98343 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d2deb25-ea46-33cb-81d0-6358d21aae82 | -14.43275 | -48.91896 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c762e27-da69-329c-ae4f-ef9212fcee46 | -9.30221 | -47.78844 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b422a8f6-500c-3241-9ebe-5ed511359966 | -13.29388 | -57.08253 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1f9fe24-d3bd-3c74-8ecf-e8c1bb625a9f | -11.1184 | -46.67167 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b3acf81-9cbb-33dc-9a2b-7b685c080d91 | -11.13759 | -55.19237 | 2025-06-20 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b41367b1-f389-3c35-9a35-f8f9ce6c62d3 | -12.34174 | -49.30713 | 2025-06-20 05:21:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6419f761-80fd-39f2-bce0-e5d62c24be1c | -11.94784 | -58.74638 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3b95b16d-fc95-30e5-99ef-58cd758552ec | -12.5539 | -57.71153 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1800806a-c127-37ca-8330-6ac1659fbe57 | -11.47349 | -47.29033 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66aff450-f72e-3440-bd32-a6250d8789f5 | -11.13888 | -46.6339 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d4111bb-c45b-3684-9bff-c9d849ddd51f | -14.44073 | -48.90394 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92729901-6373-3f32-bcee-61fbf357d587 | -11.61883 | -58.29532 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 384fcdff-f736-3e21-ba7e-184482180f06 | -10.73208 | -49.55618 | 2025-06-20 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4162ec68-1e81-3062-90db-34202d3f815b | -10.52354 | -46.64407 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b78cca-0587-3098-8db3-0babded11deb | -12.55036 | -57.71098 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd9df3d5-dde3-38ca-a9cc-169241dfb85f | -12.65161 | -54.11831 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6942dccf-34b9-36fe-8f05-c43b85fc0134 | -12.19891 | -49.62595 | 2025-06-20 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ba20c4b-f4de-3226-b5d4-cca871c767bc | -12.50951 | -58.35081 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b5c43512-5a16-3fb6-9b5f-f3fcb0246053 | -11.7979 | -48.09451 | 2025-06-20 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f71c5aeb-ee7b-3594-bcc7-53bbe32d35e4 | -11.95011 | -58.75431 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91a39099-4e48-325d-af58-a135ecfb9a3b | -9.4615 | -57.83504 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbeb4942-c71a-3b44-bb36-d83d1bcb9234 | -10.85461 | -53.77271 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2c64604-e0fd-3268-9d2a-1f3fe3b16848 | -14.30903 | -59.88728 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd1fbeea-18ee-3b47-afdf-ab3f91ae1ec6 | -9.30316 | -47.78925 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b466ea0-24b8-30d0-aee6-e6d08bf681f4 | -9.48072 | -56.08093 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 56837dfa-a0dc-3332-81b7-326bd3e9adca | -12.14382 | -54.30799 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57761ab5-c9dc-3baa-9ee4-77ae255ebd99 | -9.09614 | -50.0335 | 2025-06-20 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0dd8268-eb57-3611-888a-e6ccd3c4767d | -9.58609 | -65.88642 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d934d8-0b99-3d43-a3c9-c6e8e867cdfd | -12.51239 | -58.35516 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1294f10f-f082-3465-8330-486df6c80013 | -13.29083 | -57.07762 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8172f39-4d8e-346e-a0da-93a77cde4bd8 | -10.52972 | -46.6511 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fb1978e-7df5-35af-9104-9ac4c5b0b025 | -9.4888 | -56.07762 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b335bddd-04c2-3742-a110-c8890e7b932e | -14.03397 | -53.36469 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fb9b64e-0582-321f-8c4e-1c1bf72e4373 | -9.4838 | -56.08588 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f0e6118-99fc-36a9-90c5-71879596a873 | -9.3151 | -47.78911 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c19d30a-426c-3753-b28b-e0c4f034839e | -11.12869 | -46.66025 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8475a4b3-e4e5-31ec-bf3b-f460b6bca7be | -13.6594 | -53.94228 | 2025-06-20 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 100f68d2-5431-3505-85ff-0ac2f0b8a955 | -13.14644 | -56.80696 | 2025-06-20 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e49f1394-7402-332a-92d3-c890a291e8f4 | -12.52165 | -57.20424 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eff892dd-6428-3db3-aab6-b9c4f8693d42 | -11.61939 | -58.29156 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2c1869a-463a-3c04-84ce-c72b50d99a0d | -13.26251 | -46.81178 | 2025-06-20 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e155d94-20a5-34c2-92b6-c7752ea72b56 | -12.04786 | -62.98162 | 2025-06-20 05:21:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7032f2a8-cf42-3e5e-97d6-c68c4f10c7c9 | -12.51296 | -58.35136 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 55171c38-5846-3e74-87bb-f0cc0478a316 | -14.4374 | -48.91719 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f5befae-8f17-34ea-b8f3-fe1a961fbcdc | -11.94558 | -58.73845 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1fcee157-639d-3f90-9a9d-2a051426d63b | -9.45408 | -57.83768 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a29d2363-08a9-395d-b09d-ced97416b408 | -13.2364 | -49.83244 | 2025-06-20 05:21:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b8ff415-5b4f-371b-9a73-ee21ee73a8ac | -13.09508 | -52.29427 | 2025-06-20 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70f0034c-1194-3366-8da8-1ab8cc62f928 | -14.02926 | -53.36404 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a9cf0ba-ae5d-32d0-9036-adeadea8939e | -12.5078 | -58.36225 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ffd84f1-d628-391c-8847-aed4a7de33dd | -11.95123 | -58.74693 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1754f89e-3991-34be-ab83-04731ed604be | -12.02387 | -57.10054 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93d3d4fc-eaa5-3160-8d45-b07f8be7e081 | -10.93447 | -55.33522 | 2025-06-20 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e94f8d2-9bc0-39e7-9667-3ba06b0a4537 | -12.51125 | -58.36279 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45f267a9-231f-3d6d-a72a-c13de31b2d96 | -12.89859 | -56.98428 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99b5635c-74d8-3a28-a721-a2f009079929 | -9.4598 | -57.84623 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3705a6e-cce2-3eb7-94bc-78ced49bf8de | -12.55684 | -57.71613 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 030d5e02-85f3-3c58-a8c9-46d225a0e8da | -10.45109 | -47.06745 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20c33292-9884-391e-95ba-b1cdcccff77f | -10.36778 | -57.50785 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5aef3fc3-104d-3b78-8ed3-f5170f8e6d9b | -10.92673 | -49.27474 | 2025-06-20 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8eb48572-4bbe-3419-93cd-799ba2a3fcf6 | -16.30741 | -58.26619 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| beb208da-d856-34ad-8922-59a4db92196f | -18.99327 | -52.08298 | 2025-06-20 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9052e45a-f854-3ea7-a1b7-380d3e9bdf73 | -16.31579 | -58.25889 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d364de6b-d85c-3742-919d-2c3fad305bef | -16.30321 | -58.26987 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 284f9ebd-d782-346e-ad39-818ebc06825a | -16.29962 | -58.26935 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 653e51fb-654f-3843-b77b-4a33233deaad | -16.31639 | -58.25469 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9fee0361-875b-320b-b1ea-6525353c5c94 | -16.30801 | -58.26198 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f97914d2-6078-395a-8e78-0f63c13ecec6 | -16.3116 | -58.26253 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a017fca1-9065-32a9-8d4f-717866618877 | -16.3122 | -58.25833 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8ddfe691-9608-32e0-b25e-fe0f3001d2e9 | -16.31999 | -58.25526 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 731bf100-7401-31ad-bb0d-1cade2646be5 | -16.29243 | -58.26829 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ea615229-198f-304b-a07c-110152fca4e8 | -16.07955 | -53.74871 | 2025-06-20 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 724660b0-4ce6-3871-92d7-3f1b37d0f137 | -16.29602 | -58.26881 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c22cf115-d0ac-3418-821c-ff6e4d0da5d2 | -16.29723 | -58.26033 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 40698853-a790-3609-b127-7ceeea7a3437 | -16.30381 | -58.26564 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f17677f4-f104-31a7-a25c-5ecff7148b3d | -19.54685 | -49.6676 | 2025-06-20 05:23:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 282e95fa-7948-3397-946d-2808edf12c94 | -18.99253 | -52.09016 | 2025-06-20 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 003c0ea2-8066-371f-90b3-bf7da9ba301b | -16.30442 | -58.26142 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 8a8ee0c8-be89-3803-8981-1c4d7470bedc | -16.29663 | -58.26457 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3fe460f7-a408-3047-ad22-e1cae3059f5c | -16.32131 | -53.80123 | 2025-06-20 05:23:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc399cc0-e967-36af-baaf-af52709d7c83 | -16.30502 | -58.25719 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f54387e5-48cd-374b-869e-d8d380810251 | -16.29901 | -58.27358 | 2025-06-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 506bd4b6-2ac1-3024-8a50-9407a1bd22fa | -15.62687 | -57.30985 | 2025-06-20 05:23:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65025b1e-b4c9-3746-8eb2-7f8cc05d23e5 | -15.62313 | -57.30927 | 2025-06-20 05:23:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
