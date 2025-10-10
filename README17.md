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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f85d74b1-71da-36cb-b401-8aaff880f2ad | -14.68628 | -48.06223 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1fd52cf9-050f-3188-9ded-49be133a93f5 | -15.28462 | -46.15038 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2acfdc70-0fbd-310f-8dfa-c747304992d6 | -14.84023 | -48.46754 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0cbcc99-1e44-3a70-aba4-66f3efd143c6 | -14.89124 | -48.23321 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67342982-3e8a-3302-a4fa-eabc5f0a48ae | -14.97244 | -41.68167 | 2025-10-10 03:42:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a95bc34-c1d6-3bcf-9858-edd87fab7192 | -17.9466 | -45.02129 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa06b816-95de-33a6-897b-52b291945591 | -15.7427 | -48.99673 | 2025-10-10 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed96f4ae-56f2-3605-a7f7-77e9562c2d57 | -14.68513 | -48.06766 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1bc70225-fa48-3f50-8f93-3cbe66c2e691 | -17.21593 | -47.65964 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 305bb285-749a-3933-a5d8-5e81b96c56ee | -13.84726 | -45.85709 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| bf3f587e-8e3e-3030-bd3f-ae67e9f627b7 | -18.0427 | -44.98127 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0478e041-aad9-30ee-bf78-bdcaf49986ff | -13.83992 | -45.83424 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e96c033-7eb9-309f-ad65-c07c65c8ec2a | -13.83993 | -45.86572 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c8c300a-52d3-3546-966a-87b0b201eb95 | -15.30616 | -43.72202 | 2025-10-10 03:42:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8b3d4bc8-3387-3b85-bdd0-eee64a13d662 | -17.93395 | -45.0319 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 59ef607f-4e21-322b-979f-9e214bfa3324 | -13.36983 | -47.21013 | 2025-10-10 03:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd359e5c-dc6f-390b-be5f-081db53e5307 | -13.82606 | -45.78489 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 512c5afb-0473-3bc6-9633-ff6f87e09602 | -14.93187 | -46.77293 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0502bd28-815e-31f9-9e6e-e6b3fd33252e | -15.90905 | -43.30173 | 2025-10-10 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2443de17-6d63-3416-b4c8-1c22ffa768bc | -18.42163 | -45.24806 | 2025-10-10 03:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fd178d2-5256-335b-b27e-028cb8203b68 | -13.83909 | -45.8384 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4db370b-c738-34ff-964e-b54dccfd6b75 | -14.42787 | -48.01404 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8de87ed-ef2e-3802-a560-ddecfaa08dc7 | -13.36042 | -47.60347 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2d587db-e9a5-3e99-a994-b314897272ab | -18.01863 | -45.02201 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f4061079-30ca-349f-8934-ff5e3b2549fb | -13.29822 | -48.48941 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3450c82d-7db7-32d6-8d60-18d841b410af | -16.25106 | -47.11119 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 616af11e-d551-3ae4-9c00-ca43abd8b14c | -15.4033 | -48.04006 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8eda1613-fdf8-3737-9497-a3fc7b55bc9f | -17.93328 | -45.03518 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 53edf143-a981-3206-9d82-49fe190658c0 | -13.34311 | -47.75171 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62d21ca3-a6ad-3bf5-a175-5fd15ab8075f | -13.35576 | -47.75596 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eea7d266-396d-3869-891a-277b461728e0 | -17.92898 | -45.03059 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7157e35c-7323-31dc-ad6e-8d7bec04f870 | -14.7256 | -47.44212 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f4db20c-9e52-3504-8f50-f56914e9de76 | -15.0874 | -46.61669 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58ac1114-745c-3fb3-a186-454125f3e328 | -17.64727 | -44.43359 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e3319d5-6922-300c-9bf1-7fb50f961b41 | -18.77775 | -44.62184 | 2025-10-10 03:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e81284f7-f9b2-3a1c-9f98-b3743b6100b1 | -13.37057 | -47.20661 | 2025-10-10 03:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1d807ae-4f41-3938-aced-e170f54db3a0 | -14.94805 | -46.77195 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01adb4cc-13b7-34c7-859a-f9dd6f82a425 | -16.26866 | -47.15771 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f26b0995-3cd4-351a-9dc8-0cf7fe88143b | -14.91454 | -42.21806 | 2025-10-10 03:42:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfa67407-faeb-3d03-820b-5aa27ff62a66 | -17.39156 | -46.87062 | 2025-10-10 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f621fea-3048-3a00-bbf9-202245bc11ba | -13.22955 | -47.62175 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd3d44df-f115-33d0-8102-3225ab1dc63e | -15.09222 | -46.62297 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f29e79f1-5ea9-36f4-a397-18a6a7c8a8f7 | -13.83663 | -45.88176 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a06ff6aa-266f-3297-b422-aa60b9d00005 | -14.26656 | -45.91306 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8f4a9bc-f78e-398a-9de5-8f3d1d859319 | -14.42249 | -48.00774 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ff56aca-2a2b-3859-9b29-b8ab1c403d12 | -13.84566 | -45.86684 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abd2b0df-032c-3d6d-bc18-28a50b9b323d | -14.98699 | -47.19793 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16052f5e-bb07-3524-80af-ae9c9f6ae0d8 | -13.27198 | -48.01975 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5873fdb-14d3-33f0-a047-e92ce3911d99 | -14.26692 | -45.88625 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c7170e4-88e1-3dee-973e-33a1d5eacfcb | -15.56982 | -44.42827 | 2025-10-10 03:42:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32b8d29a-178a-3011-a096-dd180bad85de | -17.96538 | -44.95482 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d523deae-baf1-3d57-b0bf-2b42031883b2 | -16.74155 | -43.98196 | 2025-10-10 03:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8badf665-f6c8-3628-aa51-f27e0fc585cd | -15.094 | -46.61426 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63d7a7f1-2639-3903-a3bf-b1dcde2a63ef | -14.9392 | -46.76755 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b2b7475-26a4-3c9e-adbc-d0050e4d69a7 | -15.55434 | -44.32818 | 2025-10-10 03:42:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 792b1e08-836e-3299-be8d-d2da7572a591 | -15.42721 | -47.99009 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2bbf88b-ebc3-3cdf-af78-69b519a8c7cd | -18.41663 | -45.24677 | 2025-10-10 03:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d628598f-5daf-37a6-b591-8f4f45edbc18 | -16.27514 | -47.17104 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c622930e-4f7d-38a7-bcc9-b83cc9cffdc9 | -16.12876 | -42.72289 | 2025-10-10 03:42:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8e2afb38-57e4-3ad3-be82-54c5b8cd97c9 | -15.08099 | -46.58845 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5117c12c-4893-3e51-8b4a-d997f5771faa | -15.09014 | -46.62459 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b39315a-6b5a-3310-b812-0ffb2cbfbbfb | -14.71413 | -45.17894 | 2025-10-10 03:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d8a9102-e61b-323d-beae-ca9afc95d846 | -14.26636 | -45.88444 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2b1b2dc-1967-39d2-bcc5-999429680ea3 | -15.40607 | -48.03699 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c38ee87-744b-3ce6-844e-0e5de3cdc6e3 | -16.27411 | -47.17583 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff2ffa9c-fe7d-3696-acbd-97da2a5fdf3a | -13.27978 | -48.01537 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89234c59-7a7f-31ce-b61a-76b3b8efed19 | -13.3267 | -48.48795 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51a38e5c-4cab-37ca-97f2-f9954ed82949 | -13.32504 | -47.74183 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 725db58d-8f04-3563-9f78-ef1335bb2d91 | -15.40444 | -48.03474 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39b680d4-60f0-3fe7-b610-3fb2407ae145 | -15.09325 | -46.5811 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6530b583-da84-359a-a6fe-743431192ab0 | -15.38411 | -47.29666 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45725fb7-4b58-39f5-932e-e68899a98e74 | -15.09241 | -46.58507 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c48ec7-f1b4-32ee-89f2-16a5e9bbecd9 | -15.33337 | -43.19278 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d8b3e103-88e1-3717-aeb2-1e1efb6da3d7 | -15.0881 | -46.60538 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d16c0a60-57fa-3b4e-9246-b0574c26dec1 | -13.84235 | -45.85185 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| e3a624aa-7238-3e0d-9f8d-304b7381342d | -17.21694 | -47.65496 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b9974c3-f735-3301-a940-5ebdcd311db1 | -13.38573 | -44.23557 | 2025-10-10 03:42:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4be6c029-8e2f-3940-967b-c739f66034ed | -15.07995 | -46.58631 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662de54b-64fa-3c40-9f20-3856a28bdd6d | -17.93822 | -45.03661 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bc8bca6-4c5a-3bf6-898d-60d7acb8ae64 | -18.02492 | -45.01686 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 355b7f59-ac21-33de-8cb4-864fe2696047 | -17.21001 | -47.65805 | 2025-10-10 03:42:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3d0e418b-2cb5-3588-8e2e-ca6252a38f44 | -15.40618 | -47.99582 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0856112-88d8-3b91-9065-716ae74a6342 | -13.84101 | -45.83166 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13d47f9d-f94d-3a67-8dfb-d5dcdcda9b18 | -13.84317 | -45.84776 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9a67f7ea-e683-3a3d-bf5d-c35924bbe7cf | -14.26454 | -45.89773 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff47ff3a-6f23-3116-858e-6e154ac0c7a6 | -13.32109 | -48.48129 | 2025-10-10 03:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 796094da-75ed-318c-ae0c-173f168b4ced | -18.77888 | -44.61629 | 2025-10-10 03:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e270ddd7-8d38-327a-b95a-16cc804abce6 | -14.87366 | -48.22085 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ea5fe79-ed0a-3ba1-914f-c16354fae0c2 | -15.42298 | -47.99048 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61951631-6f23-346e-be52-c7c704f8bf16 | -13.83664 | -45.82092 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98912343-a47a-3f7d-8837-a3c9e8b94949 | -15.40731 | -48.03141 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d4cffe4-fe66-344c-8fe6-efbdc19dcaec | -16.17803 | -42.85955 | 2025-10-10 03:42:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33f428c-e477-3773-92c3-9dec8d40a9cf | -14.26289 | -45.87713 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb0779a5-353e-30e4-999b-6e9226272846 | -13.835 | -45.88965 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0bf9fd4-5e08-31e8-8f10-871be3956e91 | -14.26924 | -45.87505 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 962ea7f3-ac58-3778-99c4-e65f367726c3 | -13.22949 | -47.62178 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b130e2-73bd-3adc-bce7-f9e683db23d7 | -14.69135 | -48.06946 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75d73074-6a5d-3edf-b943-e1ddab3feb19 | -18.00491 | -46.25128 | 2025-10-10 03:42:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7eb569-ee82-3f0c-972d-4631d04f3cb8 | -14.93054 | -46.76704 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a87cff3d-89b1-3ae8-8b3c-57c20474a3a4 | -14.99206 | -47.20391 | 2025-10-10 03:42:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |


[Clique aqui para ver as próximas entradas](README18.md)
