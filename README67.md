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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0b21538-4834-38ec-9b90-7a5c976177f3 | -9.25394 | -43.535 | 2024-10-11 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4f3da68d-05bf-3b65-8b2d-fb65ccf88b4a | -9.25388 | -43.53303 | 2024-10-11 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3e1bfed5-6352-38a6-ac9b-5a542bc62115 | -8.93449 | -42.59184 | 2024-10-11 04:25:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b25006c6-db62-30b2-823f-ed15427b3580 | -9.26061 | -43.54028 | 2024-10-11 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| af35cf2c-e434-311e-9079-312040682764 | -9.25697 | -43.53973 | 2024-10-11 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c2c70a42-956c-32d8-8773-5dbabecf5b2f | -9.25325 | -43.53721 | 2024-10-11 04:25:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3ef661bc-f395-33cc-9933-6476f89d9e61 | -9.42955 | -44.13865 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bba6ca94-d79c-3796-8aa9-ac26da6f4d1e | -9.52445 | -42.99399 | 2024-10-11 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d990839-b0c1-3160-b76f-491121a62324 | -10.66813 | -43.66602 | 2024-10-11 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85c1dcae-bf93-332d-9245-c95dd7088bbd | -10.44616 | -44.15611 | 2024-10-11 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 700160ab-92b2-3067-941d-1505e5e79bec | -10.30111 | -43.42001 | 2024-10-11 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a022985e-4be5-38ce-b694-8789b1c0e41a | -10.30047 | -43.4244 | 2024-10-11 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97638676-3b7c-3503-ad8e-08e394608232 | -11.94618 | -44.73104 | 2024-10-11 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168c2fa4-5802-3c8e-8781-293f81740664 | -11.49137 | -43.22688 | 2024-10-11 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bd8a6af-efb5-388d-a81d-044d9c12e753 | -11.49071 | -43.23161 | 2024-10-11 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cd5630b-4d6e-3133-92ed-90c32d17ec16 | -11.10857 | -43.33826 | 2024-10-11 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8bd9417-2641-3bf0-9ad3-3fb08d342a7a | -11.8937 | -43.88918 | 2024-10-11 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00d1978d-19a7-31c4-b8ea-7e57207cfb3f | -11.78948 | -44.49661 | 2024-10-11 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a75dcb2-7a94-3587-8202-3f887bc9b74c | -11.78592 | -44.49607 | 2024-10-11 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66127546-6162-331d-bc76-289071c6d6c7 | -11.78531 | -44.50019 | 2024-10-11 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eae5e19-48f4-3e3e-9d33-3375b861ec06 | -11.76215 | -44.48405 | 2024-10-11 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91efd5e9-e1df-3f8c-9b1c-3367fe544036 | -11.75084 | -44.48656 | 2024-10-11 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6ca848c-64d0-3ce7-b34b-2ffdc1e915c0 | -11.52773 | -43.99234 | 2024-10-11 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2d36078-2e8d-3b9c-a778-4bb7b83085c1 | -11.52408 | -43.99179 | 2024-10-11 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34d65c03-345f-3433-86a7-4be60c2afe5e | -11.52345 | -43.9961 | 2024-10-11 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dae3c7b-4717-3551-a94e-c6a73a66038a | -11.5198 | -43.99554 | 2024-10-11 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 946fa8df-d1d7-31cf-9eea-d517eef491cd | -11.23355 | -44.24614 | 2024-10-11 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97f7b06f-fe72-3543-b4bc-23d83b795caa | -13.1155 | -44.07926 | 2024-10-11 04:25:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 723c1603-32fb-351f-8403-33e947397bbf | -12.778 | -44.86938 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ee88ca1-3c14-3a4d-9673-b590d1f5fb5d | -12.77681 | -44.87751 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52fd7b98-db76-3829-bf16-b898b6134957 | -12.77563 | -44.88564 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fc4a8907-843d-3c37-8493-fe260273d0b4 | -12.77505 | -44.86477 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9423d9d6-8cd0-3708-8464-da90bd5e807d | -12.77446 | -44.86884 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 736d3dd6-9a54-347e-96e1-1e5a81356e2d | -12.77387 | -44.87292 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87622581-e044-3600-8dc0-97d985772e2a | -12.76738 | -44.86776 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12716518-b49a-3024-a502-1f1aa697e122 | -12.65544 | -44.24483 | 2024-10-11 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a199985-920c-304c-b927-c2581b510f9e | -12.58357 | -43.36501 | 2024-10-11 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae9ebe32-bcb7-3ee2-9c28-eab7b1f16d0d | -13.36551 | -44.77856 | 2024-10-11 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9160ad9b-898f-3572-8d0e-1ddf9df05413 | -12.78331 | -44.88264 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35fee6b2-accf-3f26-b536-7fdeac901192 | -12.78271 | -44.88669 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ca5ba42-cd33-3b5f-98fe-6e55e3be301a | -12.77504 | -44.88969 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15a2d094-6876-342f-ac56-ff01143c432f | -12.77151 | -44.86422 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2137ce5-2041-333a-b48c-d74758983c33 | -12.76973 | -44.87645 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 93c1d610-65cc-31ee-b6b3-12a15f6ba901 | -12.76619 | -44.87591 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe986584-7126-35f3-b400-c563d2281167 | -12.58289 | -43.36982 | 2024-10-11 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f69ea52-1dde-32c4-86e8-c25379ad94df | -12.4326 | -43.74775 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8438d8de-b838-3acc-bf42-11bd866e930d | -13.70784 | -44.44997 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f88f6f7c-75ef-3d7f-b4c1-24ef0d887648 | -12.37582 | -44.11483 | 2024-10-11 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0719a37e-ebcf-3d45-b8b9-9fd40fd00f73 | -12.35406 | -43.75318 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f2d33593-98c9-3eab-b7d1-aa8cc958e9a5 | -12.35339 | -43.7578 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 75b4d837-9a70-3278-bfe7-32f459bb6bf5 | -12.35148 | -43.75495 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 6abc1787-cb27-34fa-96fa-b6c71027b527 | -12.35083 | -43.75964 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41346d96-82a4-320b-b33c-a7b40c84f046 | -12.35031 | -43.75277 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 442a4155-84d7-33c8-bea7-1bda0bd9935e | -12.34962 | -43.75745 | 2024-10-11 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cdad3b0e-b33b-3727-bcba-ef3ada327cee | -13.37537 | -44.68562 | 2024-10-11 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4eb6d53-c308-3a25-abe2-b94f3c951ed3 | -12.77741 | -44.87345 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28cd3436-6530-3421-bfa6-47d9510a7c05 | -12.77268 | -44.88105 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c50ce5a8-a4e2-34ef-93c5-fac42e36b35f | -12.77092 | -44.8683 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1b8e6fd0-cf83-32f5-90df-f22655b9e056 | -12.76914 | -44.88051 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a5ad48f0-bbe3-3ab3-8c2b-c23a85b170b2 | -13.36909 | -44.77908 | 2024-10-11 04:25:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 357264cb-33fb-315e-9158-80e2f7466ba2 | -12.77917 | -44.88617 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6ab4cbb1-5fea-3f57-a803-335b920fd153 | -12.77328 | -44.87698 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 68b7d132-b3df-3a43-a11d-6f1ad1e721f3 | -14.18949 | -44.36885 | 2024-10-11 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e82ade8c-06c7-33fe-932e-c1a50d45840d | -14.04978 | -43.6927 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f1d10a6-e799-32df-8cf1-d25a51242124 | -14.48555 | -44.96146 | 2024-10-11 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e58646f-c28d-3d8c-9eb1-c03a712de153 | -14.36376 | -44.66188 | 2024-10-11 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f21d209e-1ba0-319b-afce-29ff0a30c380 | -14.18885 | -44.37331 | 2024-10-11 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa6967e4-9b03-3cd8-9a29-d8ec2ebb51b2 | -14.04061 | -44.03725 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc745503-95ec-3a5a-b3c0-fb5726fbf169 | -13.91718 | -43.81386 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a012ebd-0ec1-39b1-80d8-9ddf6eb1d70d | -14.07344 | -43.69117 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbcf41c8-51b6-3fb3-9712-e162bd1bfc30 | -13.74738 | -44.46048 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0290a834-35a5-3be9-b128-d1b034c45cc2 | -13.74674 | -44.4649 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4c7057e5-b009-3707-9c6a-385a7f2fb37c | -13.74309 | -44.46434 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34306e0a-dbd3-3bc6-ae02-4d33ef4564dd | -14.08769 | -44.1384 | 2024-10-11 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a25f786-79f1-3eb5-a0ea-44999fa16e74 | -14.07276 | -43.69601 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d83aa88-5deb-3eec-962d-82c9b07786dc | -14.04216 | -44.16448 | 2024-10-11 04:25:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed94c7bb-de7d-3f33-8382-fd226cce3ef4 | -14.03945 | -44.03915 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f9950ec-d94f-3680-8067-c5daed8be0d2 | -13.92098 | -43.81442 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89a652c2-121f-3c86-8727-cc51d97d2abc | -13.92031 | -43.81916 | 2024-10-11 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88aba029-2c9e-3342-b05c-b5a526baf566 | -13.84433 | -44.19693 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a93fad5c-eefb-3544-a1c7-ac3c98c52adb | -14.71595 | -44.8098 | 2024-10-11 04:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c34a663d-90d5-374a-8da2-e54caffc8b25 | -14.06641 | -44.94283 | 2024-10-11 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed4f0e34-00f8-3b3d-825f-f9fa6542fb52 | -13.80742 | -44.64058 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b06148c1-77dd-36ec-83b0-c0ac35722c77 | -13.79717 | -44.63462 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5a925fb-1de1-34d8-834c-21b86573001e | -13.79355 | -44.63406 | 2024-10-11 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d808977b-4e0c-3882-9f60-f7752506b575 | -14.06581 | -44.94698 | 2024-10-11 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ff0504-62be-3213-a172-d4af75f2af51 | -8.40189 | -44.02621 | 2024-10-11 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41a67440-ba80-35a5-9c1c-495ab36eb887 | -8.39837 | -44.02568 | 2024-10-11 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2933bb90-7848-3ef8-abcc-38f0f4dc01ae | -8.39777 | -44.02965 | 2024-10-11 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb89d690-78e9-37ed-8ea6-b2c4c4901811 | -9.98553 | -45.14376 | 2024-10-11 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4f5bf61-179f-3dd6-a769-5962d7a243e6 | -10.8234 | -44.9454 | 2024-10-11 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99da0e52-cea7-3be5-8047-0cd0997b971e | -10.72891 | -44.78091 | 2024-10-11 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23b02c2c-9cdf-33c6-8c92-e113d3133b28 | -9.57939 | -44.39537 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cecb4c22-4265-3716-bdd0-f9ff6d566056 | -9.57589 | -44.39482 | 2024-10-11 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f5e3a488-3c41-317c-be39-21cb535286c4 | -9.98518 | -45.14455 | 2024-10-11 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4bc7bfb-7050-31fb-b074-b3af7915979a | -12.31874 | -45.31048 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5135c08-0cff-35a3-8ba2-f9b66dba0f81 | -12.31816 | -45.31434 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba97a7f0-1348-3bfe-b907-d50068bc6b7f | -12.31528 | -45.30994 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ba14e78-42a6-3c76-9c32-f4fa7e89c5da | -12.31471 | -45.31379 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67747680-6bc9-3a76-97fc-7d3e3eeef00f | -12.3124 | -45.30553 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README68.md)
