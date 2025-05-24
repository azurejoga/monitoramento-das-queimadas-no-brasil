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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cb7d046-10f7-34ba-ad14-7cb3b7b3971c | -13.7138 | -57.48317 | 2025-05-24 04:59:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85f81dfa-69f7-3411-b816-89c0e2557d40 | -13.82753 | -59.69341 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b38b26d8-7765-3178-921d-c42a23bd7a9e | -12.37005 | -54.90027 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa756ee5-f25f-3d86-9eb9-d4eed3162dcd | -11.76259 | -54.22682 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 593f8e5f-d652-3d57-9da2-ee2735129479 | -15.62918 | -57.30805 | 2025-05-24 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea937e32-3ccc-328c-8b86-bab75fb751b0 | -13.37029 | -54.26638 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba7d615e-2e7b-3434-b99d-be7e4fb67c15 | -11.6705 | -54.93651 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39c99269-1bfd-37ae-97c5-3175fadfc4aa | -15.48152 | -59.43285 | 2025-05-24 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d151ef7-acd8-3f65-b337-253af1a396c6 | -11.76204 | -54.23042 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f76ccfde-a91c-325f-a60e-1dfe51cb6fae | -12.13717 | -54.66708 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 972680f8-7d4e-3569-8e2e-6fb91a18dc3f | -11.99596 | -57.21663 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44e0af3a-a3fe-3f0a-bef0-c2026f146fb4 | -10.68507 | -57.60054 | 2025-05-24 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e3edd7-8363-320f-9081-f4e1ef34539a | -13.86242 | -59.72571 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c2a81eb-7e25-3e1b-834a-1fdaa2de0451 | -11.42141 | -54.30226 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96a3e172-29d2-3297-9f5a-27130f9172b8 | -12.35506 | -49.92614 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83a2b31-d363-3720-b773-0a891427d0aa | -13.14807 | -56.81299 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d85e57f0-e128-36d3-9a07-6e7f1a5ced79 | -12.35817 | -49.93457 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc439988-7b3c-380f-b848-ed314eba77b0 | -12.19471 | -54.26841 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aced61b-9310-36dd-87d4-553dbfed6614 | -12.02815 | -57.10449 | 2025-05-24 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f40381dc-b165-32b0-ac1e-5a384ce871f5 | -17.15385 | -54.00729 | 2025-05-24 04:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82e68a56-7ecb-3e15-bebc-433ab61dbd2a | -14.03696 | -55.13631 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76e295ee-b108-3d30-b404-74b22a0fa13b | -13.14864 | -56.8094 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f64eb91-363e-3a22-92a7-d427fa4040bd | -11.8073 | -57.35741 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 450aa579-b41a-3cdd-812a-39e448fb5c8b | -12.03569 | -54.97359 | 2025-05-24 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29274e4f-2984-32a6-b358-edeb0dcb68d5 | -14.02976 | -55.13884 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9af9fc8-5307-33ac-a42f-e1cfea24f81a | -13.8525 | -59.72579 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beeb75ae-f2ac-32ba-b226-6aaf937b5f59 | -12.37998 | -49.99277 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4591c6ca-d06d-3296-a750-65e27bcbb79d | -14.06694 | -57.11088 | 2025-05-24 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 69c7ec26-2e8e-3170-a7e4-f7cfac4cd81e | -12.41853 | -54.38436 | 2025-05-24 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aaeb16f-6650-39b0-8f3a-818d21ca0534 | -13.81431 | -59.68174 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bfec3eb-05ca-3139-bc9b-89a13c89e78f | -15.6286 | -57.3117 | 2025-05-24 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fe3d7e9-b10d-3da8-b9d8-87e766a8f1d2 | -12.40483 | -49.98013 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2f8e5c60-1970-33dd-b619-3773146ad220 | -15.07885 | -48.94279 | 2025-05-24 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3afca4c-55af-34eb-a579-02e62bccd5f6 | -11.62588 | -54.94021 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18e4eef-7488-331a-81f4-09711b6db69b | -15.63251 | -57.30861 | 2025-05-24 04:59:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7a86dbe-51f5-36cb-804b-51a91b33c01f | -13.19514 | -53.58087 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8813fa7b-f126-3a3d-b2ea-24ef6c911101 | -13.36691 | -54.26585 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b993fecf-d8d7-35b1-b7d4-dcf8231466ed | -14.01925 | -55.14082 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7de770b3-326d-31b7-9961-c2dcc5ba9b7a | -13.67218 | -53.93401 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a14e5e93-429d-36f1-b5fb-fe27a58d2b57 | -11.6738 | -54.93703 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41661e5-7d80-3fad-906b-2635e2a93b20 | -14.03973 | -55.14042 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 904af95e-fd66-392f-8758-03b7b0e7629a | -12.13772 | -54.66351 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f69a70b-65f6-3670-8def-317c9df3f259 | -13.15473 | -56.81409 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 78d99295-da8c-30bf-aae8-633b4be480c0 | -10.6816 | -57.59998 | 2025-05-24 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11013687-076f-3042-9576-5ef8fb878e86 | -17.14626 | -54.01026 | 2025-05-24 04:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed5a96ea-a7b0-35af-8e4b-711fbdfcc37e | -12.3587 | -49.93065 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 825078bb-e8ac-3574-bead-95f98996494e | -11.75534 | -54.2294 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1b437d89-ff62-3304-ac81-9f894c5f9943 | -14.02699 | -55.13471 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c827065e-4341-3055-be43-423ab63765e1 | -13.15082 | -56.81713 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6245b0cb-b9cd-3591-be4a-c6f6be64c1b4 | -13.4577 | -47.47854 | 2025-05-24 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02f935e3-13fa-3255-9ec2-736c866515e2 | -11.88393 | -56.41651 | 2025-05-24 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42257a5e-a89e-38a0-9fe6-ed753ca89d0f | -11.75589 | -54.2258 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b52f41ce-e764-35ac-97c8-50a6c95163fe | -12.13549 | -54.65586 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be2805d4-0fef-3516-861a-5c045f546799 | -13.36465 | -54.25794 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 33d6d4a6-35ba-3597-8b33-c42b7c92894c | -12.5314 | -54.88943 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c48a707-5278-3791-a901-d959826f4e1f | -12.40534 | -49.97623 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 125eae32-420b-34fe-804b-cbc69b5b122c | -12.64435 | -57.18767 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59117b38-cc5d-3921-a5d8-ce726e48711a | -12.64375 | -57.19133 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f73789c1-f21a-3d5d-b19c-aa594ca9c1cc | -13.85213 | -59.71918 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ad821bc-e1a4-3f3f-adad-58164f621b88 | -12.75914 | -49.31971 | 2025-05-24 04:59:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 645b1e3f-4b3c-3066-b24f-f5e78bb39eee | -11.57235 | -54.55944 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01579765-ee1f-3b6e-9478-0b9def7642c5 | -12.83609 | -47.39084 | 2025-05-24 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7531ee09-9e93-3c86-9763-858ad4cde125 | -11.4242 | -54.30636 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecbbe44c-e66d-3d08-aba5-3b6a6556c4ff | -11.42475 | -54.3028 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 884e808b-6d86-30e1-a34d-d775654d98dc | -12.35089 | -49.92551 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 296eb095-a8fb-3031-95a0-90d355e0da1f | -14.07086 | -57.10784 | 2025-05-24 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a2dfbfc7-09b4-36a2-ac2a-dc9534a8c9aa | -11.42087 | -54.30583 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da9f5c0f-8853-34dc-8e7d-882be4896769 | -17.27079 | -48.62085 | 2025-05-24 04:59:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cf85cfa-699b-34e5-bb6c-abba30994679 | -13.71717 | -57.48375 | 2025-05-24 04:59:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9308117-e5f7-350e-a6b1-ae341fd190dc | -12.08572 | -57.37627 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 175bde91-9b0d-3719-b572-d1efff618436 | -12.40288 | -49.98052 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42ad29e0-526b-3d08-aa98-2371fe5ab74d | -12.35453 | -49.93007 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0bec9c2-4e47-36f6-a95c-18967b474970 | -12.67181 | -58.21958 | 2025-05-24 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80277f8c-0554-39f4-b7b8-d12f836edecc | -13.85873 | -59.72504 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62e33fd5-be34-3800-a9b1-a9eafd1c982e | -11.29967 | -53.98136 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f86a0b3-04e4-3b77-81c4-54d1d713d71e | -12.41201 | -54.17887 | 2025-05-24 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca74216-a366-35ba-b0f4-28dbe72061b5 | -9.96303 | -64.937 | 2025-05-24 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abec985c-41aa-3adc-8dba-a5ddd8d77916 | -12.08851 | -57.38058 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13ec398c-f965-3a05-b4a9-6a8cab92f2f3 | -14.01703 | -55.13311 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50384f14-d36f-39bf-afbd-e7482d7e9f8f | -11.35829 | -55.13112 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e758201-9064-344b-89cf-1a12297dcc1f | -13.36636 | -54.26953 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 17113728-ec34-3be3-96b8-0482dc9cbe73 | -12.17515 | -54.26165 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef2d0f25-a6f5-3c94-b73d-8da66a44f756 | -12.40066 | -49.97956 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4447a46a-91ba-39f3-b7a5-9a8dc2a9309f | -11.99656 | -57.21292 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a63f443-ab0a-39ea-a719-7ec7e8613293 | -13.86084 | -59.7348 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5eda870-e2bb-3c6b-9de7-cc5b5c67bccc | -15.83614 | -58.56004 | 2025-05-24 04:59:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 52c6b0e7-fde9-3585-8983-73e354337a83 | -13.14474 | -56.81243 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 55e04839-a46b-3ae8-bd3c-075e0266d244 | -12.39402 | -49.98321 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81183651-1eec-3e05-a67f-81fef5d9add8 | -8.07 | -43.1216 | 2025-05-24 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 320199f7-b1bd-3cc4-93fc-08e73b352b30 | -21.95949 | -56.07834 | 2025-05-24 05:01:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a52debc8-6325-3503-b298-b94c2e801d6d | -20.94125 | -56.59131 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ac68c96b-4e57-3896-b05c-6f14aa30f7d7 | -19.60216 | -45.0192 | 2025-05-24 05:01:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9a74761d-31e9-3fd2-9fbd-303aca879fbf | -21.22172 | -48.61214 | 2025-05-24 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ac90472-6efe-357f-9f33-723a9da20148 | -20.94459 | -56.59188 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 123edd3c-1933-371c-8cb4-aa61c9f8b10b | -19.79358 | -53.83745 | 2025-05-24 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0bbbc33-a20b-35ae-b966-4f53fc4a7d25 | -23.55028 | -47.63749 | 2025-05-24 05:01:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd60c596-922d-3d82-b610-c057de43d549 | -19.87367 | -54.36519 | 2025-05-24 05:01:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff7ef8ad-5a4b-3037-8b69-642ddf3f1e7b | -20.47904 | -53.67397 | 2025-05-24 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b493ca1-102f-3fe0-b09e-eec7a9b36f05 | -20.94849 | -56.58869 | 2025-05-24 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ffe1018-769e-3213-85e7-5d5f27334dfa | -18.58757 | -55.9384 | 2025-05-24 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README16.md)
