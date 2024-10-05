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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82ee7a2c-119a-3e92-86bf-7d46c4b0551e | -8.39571 | -46.31432 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72ca8f05-a234-3434-92ae-9176f7a72daf | -8.60405 | -46.49441 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 983f2cba-a680-3e71-b521-8f64d80c5e53 | -8.58822 | -46.50082 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6f2ac1ad-01c6-32a7-ad02-705c18fa9157 | -8.5877 | -46.50312 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19b23c59-c33f-3dc5-9463-950e79d5dd5d | -8.43677 | -46.43818 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17cc58e9-a8af-32fa-a860-160df673dbeb | -8.43312 | -46.43766 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecb5083a-0bb0-38c8-bf80-4aa20f5221ea | -8.42087 | -46.4448 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47e33c57-89e0-3641-b791-9027498dc5e0 | -8.41748 | -46.28892 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d089089b-dc07-30c0-9c66-e85901dd7a90 | -8.39635 | -46.31001 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 128035d9-ee3f-3eb3-bfd1-a806cfc2fa43 | -8.39269 | -46.30942 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cb02e24-abf8-3259-b19b-29540fb97b40 | -8.76783 | -46.8052 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2739737-50b8-3258-8fa0-84cc92f8da08 | -8.5005 | -46.86184 | 2024-10-05 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e3a888-4825-3928-aa75-ea6878152886 | -9.88855 | -47.19608 | 2024-10-05 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fae9dedd-9a9d-3452-b8cb-468d440c4f9f | -9.87723 | -47.19853 | 2024-10-05 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 067ec705-fda7-3c89-8fe5-987dd28d5bbf | -9.87304 | -47.20211 | 2024-10-05 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7059a333-59cb-3af3-830c-b701a30968cc | -9.86947 | -47.20159 | 2024-10-05 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35f3fd85-53c7-32e0-be57-801bc1352aa4 | -9.84005 | -46.72248 | 2024-10-05 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6f5a90d-d11b-39c6-858a-9f305c34ea8c | -9.8394 | -46.72684 | 2024-10-05 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2920d0ef-8487-354f-9ffe-661e3b3eaed6 | -9.83574 | -46.72629 | 2024-10-05 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d41ad6f-c490-3786-a5ad-7f9ab222a7f5 | -9.8351 | -46.73061 | 2024-10-05 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37e139df-04c8-3155-a61e-c72445e09972 | -9.83145 | -46.73005 | 2024-10-05 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e73e3666-0ea7-3174-8418-4175700277e3 | -9.9725 | -46.35222 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da5fd663-1f87-3b7e-912f-0bcceb47b16e | -9.96808 | -46.35641 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c0fa05-bb07-3478-ab44-cbbab4fd3753 | -9.77923 | -46.06039 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 841a486d-7ea4-3a41-a9b7-2466d7c0dc34 | -9.54659 | -46.12037 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a3e98db-d95a-30c8-9c15-40e72bee46c7 | -9.54593 | -46.12495 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2ee91501-03e0-3d80-b0e0-d938722a6b75 | -9.53362 | -46.496 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ad0417-28b1-3d40-9d7b-11f42af981f5 | -10.75739 | -46.1878 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4f903b7-1e4a-3947-96e7-8a7e4dc54aba | -10.7567 | -46.19256 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d90be920-bbb0-3607-825f-0b2ee655b455 | -10.84156 | -46.32637 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02f70a34-d661-3074-8a3d-243a790548c4 | -10.54317 | -46.28058 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6044f593-30d7-3a64-adf3-063fd819ffe6 | -10.53939 | -46.28003 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52bb96c6-8da4-3b9d-82f0-69e499d6a0a4 | -10.1551 | -46.34772 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dac208f0-7903-3a33-901f-704b31f8527a | -10.15071 | -46.35164 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaa1fadd-4a5c-337f-9768-34d1afe96b86 | -10.13949 | -46.34985 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cc37115-0942-3e36-81a4-b86f28e77bf6 | -10.13575 | -46.34924 | 2024-10-05 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2929157d-fcd9-3e4a-9355-83146f0e5f69 | -12.04403 | -47.37891 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ae75193-6d00-3d1c-a018-20bcbd62e697 | -12.0398 | -47.38261 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f05ac67d-757a-35c6-b6e5-a6cfdfda526e | -11.42119 | -47.19515 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86ae1d4a-0d1a-3e0a-9364-e3fe0c31b41a | -11.41666 | -47.19579 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fcc29db-0f71-3766-9b2c-68b0425168db | -11.41209 | -47.20687 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79e2034d-9f2a-3afc-90a9-2681d1fb52d3 | -11.41113 | -47.20802 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5852f6d6-96c7-3e3c-b902-31eb39b6ab66 | -11.3807 | -47.23837 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e30fa5a-9ab4-34dd-bd78-97500badb72f | -11.37771 | -47.23354 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f700a76-d7d6-3d9f-8bab-a435066eddb3 | -11.37471 | -47.22872 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 165aa325-4c60-35ac-990e-cc9907d62d04 | -11.37234 | -47.21963 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4707020-9ab3-3558-8348-09398a9305ff | -11.36696 | -47.20578 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57e287e2-1755-32b1-8b8b-a7b991929bf7 | -11.36031 | -47.20048 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d31b26da-2483-3270-8159-a98e144572de | -11.34904 | -46.84558 | 2024-10-05 04:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d71f8e9-415f-3564-8acd-85547ab7bd4e | -11.28263 | -46.80839 | 2024-10-05 04:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e605ea9c-b77e-3978-bfb7-8471d919ce1b | -11.26278 | -46.99899 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 891a4d16-ef6e-31d4-ba27-18ea8b313b58 | -11.24446 | -46.99627 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 548c5b94-613e-3276-972b-db7d5983bfab | -11.24204 | -46.98703 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d6a0a73-3074-39a5-86b7-4aa642480fda | -11.24142 | -46.9914 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b4c53aad-9965-32bd-8a08-3f55d55fd5a0 | -11.2408 | -46.99576 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 78947496-72e3-30ca-87db-e27cc3d66cdb | -11.23838 | -46.98648 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a0578eaa-b84b-307b-a5be-d0f33860175e | -11.23775 | -46.99086 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9510b127-766d-3a74-a246-8ade3a0978f1 | -11.23347 | -46.99469 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8204b9d5-9ac5-346e-9b58-918425ea2f41 | -11.23107 | -46.98677 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 2afb0b4d-a645-32dc-ae3b-a4f8f018c80f | -11.23043 | -46.98973 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 82e00ef2-bb7f-3335-8387-4890cd2f9388 | -11.23042 | -46.99115 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| abfd6c13-1814-3fd9-85b9-f29944c61d56 | -10.92263 | -46.67207 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c4924c-f459-3210-bed0-462549a7a0f8 | -10.91825 | -46.67603 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea3a5bca-399f-376b-989e-ed573d7a2650 | -10.91454 | -46.67547 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d873c92d-0882-3637-bdb8-ac48836e6a57 | -10.91083 | -46.67492 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cbc1087-fece-39ae-ba0e-31f1da4d4713 | -10.88633 | -46.63441 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4200a4da-0664-34b9-9b05-6ca21e8ab1a5 | -10.88082 | -46.61987 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d4aad48-e18b-3d60-a7a5-063b74f205c6 | -11.2319 | -46.61942 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48a4ce28-2c31-3318-a03e-59bb85d83dd5 | -11.22882 | -46.61428 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d16f5fca-1dc4-30a4-b43d-1edfbdd806e9 | -11.22817 | -46.61883 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0148254e-944f-3736-aab5-371217618c4d | -11.21956 | -46.599 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e608a4f4-9a14-33fa-9218-3d3c47007936 | -11.21582 | -46.59842 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3deac7dd-f2d6-33d8-8c85-c0330e6c9ad8 | -11.21517 | -46.60296 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39542234-3cd4-3078-ab12-1407a492418d | -11.15891 | -46.50932 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa3eef36-65f3-3351-bb5c-5dca002f157b | -11.15519 | -46.50851 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0475deb1-3231-3265-b579-6605f18a96c6 | -11.14771 | -46.50717 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79a9c70-59de-3f7a-87fe-0e3257525186 | -11.14706 | -46.51166 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3753e2-a480-394c-b852-cd9a01bbb6c2 | -11.14331 | -46.51111 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a33658e8-56bb-370b-bf31-0932016ce910 | -11.13955 | -46.51057 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd87c11-726c-3762-9f3e-f443e7c14d10 | -11.13889 | -46.51513 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0f163bbd-6883-3dcb-a1c1-30a0b471225f | -11.13513 | -46.51457 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a71cfa2f-06c0-3601-8709-78cc78d457f2 | -11.13138 | -46.51398 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 564addf6-802d-35e2-8795-12a06a70aac1 | -11.11946 | -46.51693 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fcd0d404-96bc-38f6-9ee6-496e4ae43421 | -11.11881 | -46.52146 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 807a7568-b65b-392b-be46-d0d45bace5d3 | -11.11635 | -46.51181 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f73e5ca-0818-334e-b846-88dde8580733 | -11.1157 | -46.51635 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77f29119-015b-3ac1-a513-ab9a765a1112 | -11.1126 | -46.51122 | 2024-10-05 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74d02bac-ab8a-3fc6-aff2-7b12020bbce3 | -12.0393 | -47.37943 | 2024-10-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a36b92ff-99ae-341e-b8d2-cd12b1e32ba2 | -11.7421 | -47.70047 | 2024-10-05 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e2157bc-fdf2-343a-88cb-626b078fc84c | -11.71798 | -47.10307 | 2024-10-05 04:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e32f00-05a0-3bf5-8417-aabf3bf6911f | -11.56101 | -47.43482 | 2024-10-05 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97ea7b51-9459-35e8-a1d4-83f16e09d1bf | -11.42482 | -47.19568 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75923dc3-8557-32cc-a5a8-a3ce36768cf5 | -11.41391 | -47.19411 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c90c275f-7178-3d0d-a4ee-9924e42045c2 | -11.41303 | -47.19527 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e9a019-ba56-3e9d-ba43-d6580b3e57ba | -11.40939 | -47.19474 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10750c8e-d730-3405-83e2-b0a469983594 | -11.36093 | -47.19623 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e330f030-dee8-353a-a58a-0ce144b4fa68 | -11.3597 | -47.20473 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c730741c-e817-3dd6-af4b-a86a27bf332b | -11.25607 | -46.99359 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f826842-ac7b-37ac-99d6-2aeab6edf3c9 | -11.24508 | -46.99193 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3560eea7-7315-3e16-9ee9-3aed163c93e1 | -11.23713 | -46.99524 | 2024-10-05 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |


[Clique aqui para ver as próximas entradas](README99.md)
