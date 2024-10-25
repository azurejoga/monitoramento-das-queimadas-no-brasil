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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de630bea-bb01-3ff0-aea5-cd7465fae5d1 | -4.18658 | -40.63159 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| f93e1ea6-45ea-30e5-bbb3-399da6ab5d41 | -4.18595 | -40.63112 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| b946151b-a3db-38ac-87c8-145bc6110763 | -4.1859 | -40.66159 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 34084074-df42-39be-9be8-5005a7447e70 | -4.18587 | -40.62752 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| b3f8c403-4890-3816-8446-295391a987f8 | -4.18579 | -40.66558 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 3204ef3f-c0b5-36ec-a1d4-cfc8c629fc16 | -4.18526 | -40.62704 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| ad4ac558-ac12-3d48-90ea-f6e06fe83261 | -4.18505 | -40.6612 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 7676b45c-eb3b-3a7e-9a33-3800aa19e710 | -4.18236 | -40.46637 | 2024-10-25 16:52:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 19127604-e12b-3edb-b15e-b5b5cfee2993 | -4.18187 | -40.46738 | 2024-10-25 16:52:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8dc5cdca-960e-3ba6-b09c-38e0a5393465 | -4.18081 | -40.63253 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 70579228-b24c-3005-857b-99b779406a62 | -4.18017 | -40.63208 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| a152e8b2-ae69-3349-8b54-9d46ae6f0c01 | -4.1801 | -40.62845 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| cd8f3e8f-7a5e-30a1-adf7-4baf0aaeb87c | -4.17949 | -40.62799 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 5631e735-e912-3afa-9356-e9ed18441e53 | -4.17371 | -40.62894 | 2024-10-25 16:52:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 3f02dd34-a55c-3d93-911b-8db4a6946711 | -4.08883 | -40.2691 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e3290da5-db69-33fd-91a0-3c630aa9fdf6 | -4.02063 | -40.19191 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a1f43583-9c7d-365e-ac3f-02d3db070fea | -3.95683 | -40.44441 | 2024-10-25 16:52:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4fb4cc26-675b-3512-b373-ab1b5bec7c02 | -3.81799 | -40.28418 | 2024-10-25 16:52:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 158cc593-0b0b-39b7-970b-2a0085fd7bce | -3.81572 | -40.28531 | 2024-10-25 16:52:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 0f20bd5f-22b0-3f01-a5fb-ba9f9fcb08a2 | -3.78905 | -40.29351 | 2024-10-25 16:52:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 399e2054-1130-3f06-843a-658b2c70c04d | -3.70412 | -40.53439 | 2024-10-25 16:52:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e833818b-39ed-33af-8005-f96710c79e03 | -3.69596 | -40.77293 | 2024-10-25 16:52:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7112c945-af22-3497-9d4b-59f7465c47cd | -3.69145 | -40.77547 | 2024-10-25 16:52:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 510eebf1-e174-3628-bd12-b6d0843efba3 | -3.65145 | -40.40193 | 2024-10-25 16:52:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 9b9685b8-66ce-3f95-b6cd-3b9ec59bc175 | -3.65067 | -40.3974 | 2024-10-25 16:52:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| b595ef17-2a08-3499-b080-5fe3d4925e61 | -6.1252 | -41.10122 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 15857e60-43a0-3f4c-aab2-1ac352a4c128 | -6.11359 | -41.06727 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b2605539-3179-3eb9-addc-8e816255cbf5 | -6.11298 | -41.06381 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 66354209-e28b-3db5-8cfd-8945c366dc30 | -6.1116 | -41.06543 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 77292a91-db24-3e84-8c2e-a3c7a9419724 | -6.09194 | -40.62136 | 2024-10-25 16:52:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 3cf2f5eb-5ea1-33b3-9711-000ea3fdad27 | -6.09128 | -40.61753 | 2024-10-25 16:52:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 52eb9722-8888-3108-820c-8f52510dc24f | -6.07606 | -41.11887 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 474af5de-9405-3fba-bdf7-ecf2121d0699 | -6.07066 | -41.11993 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6aacb1b1-5d0d-3485-835f-43850b1bb96a | -5.98849 | -41.00311 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 4b760426-c04a-32e4-9035-e258061e81b9 | -5.98752 | -41.00183 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| cc59599b-2b81-38e0-8035-70d69e514a50 | -5.93826 | -40.67875 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 13a697c3-a9df-3af3-b066-add71d3a8d97 | -5.9369 | -40.68099 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| ac6aad6b-fa28-37c2-9a2e-a8aba032c67c | -5.93623 | -40.67725 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7e3bf714-c998-3c72-b0f1-a3df0b50afbd | -5.91894 | -40.66677 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c7b1fa77-8685-362c-8d14-644a50dc7a6f | -5.91679 | -40.66518 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 76df987e-314b-3050-a11a-9510b5cb18d0 | -5.91302 | -40.57946 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6255ab82-5088-35f9-a241-ea108dba4fae | -5.91015 | -40.58178 | 2024-10-25 16:52:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e3751f5f-9fa0-35cf-be25-07e91daa05f8 | -5.90304 | -40.70813 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 95fd4da6-9468-3c11-8f97-523e601730e7 | -5.89738 | -40.70867 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9e88ec24-bb5a-38ec-8c61-994302b2af6b | -5.88492 | -40.99524 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ac29578d-6f13-306a-8a9d-a7ec697b1f96 | -5.88429 | -40.99168 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7d98f5be-2959-3c6f-a3e0-6d1bfbae8f0b | -5.8838 | -40.99289 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7759d6ec-ef4e-3a45-89f0-087da0331185 | -5.869 | -40.96918 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 9aaca498-ae4d-3f1c-ac11-6a4c2139350d | -5.86868 | -40.97037 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d89ec80d-e09b-3792-84f5-0415885a3374 | -5.8681 | -40.96695 | 2024-10-25 16:52:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fd733135-02c8-37fb-b2a8-229972b37e32 | -5.86632 | -40.88984 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6229937c-a4de-39cd-8457-878d89bb9143 | -5.83117 | -40.85054 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1c6b90fe-363d-3cf8-b4f7-e1636beacaea | -5.83052 | -40.8468 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 58b7186a-843a-3b32-bcc9-80d5c0d5d621 | -5.80726 | -40.67769 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| e696b34e-dfca-304b-984e-a093e0aee3ef | -5.8054 | -40.67713 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 3417d4c1-8946-3697-b217-ca3b5a942d24 | -5.77159 | -40.60502 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f024b510-6b87-3860-9144-1d199f4698a6 | -5.69591 | -40.68947 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8bc678fa-8106-3569-a03b-08d211d20a65 | -5.69274 | -40.45462 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 9638b8fa-f641-31bd-814f-0bee2970f6e9 | -5.69205 | -40.45071 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 620edcc8-9820-392e-9658-c14d7c66e695 | -5.66496 | -40.71083 | 2024-10-25 16:52:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 4305a48e-7d99-306b-9bb1-a90f61ba50c1 | -5.65936 | -40.71181 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 3d7dee3a-5f04-39c8-bceb-b312bfadf00d | -5.6574 | -40.76652 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 4d7a6321-7ef4-350f-9fe5-ac64ecd36044 | -5.65675 | -40.76282 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 4104c035-96f0-3912-a0fc-265789018956 | -5.52869 | -40.80292 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 2dbbd9e1-d585-31f5-b1d5-f5280e088393 | -5.52804 | -40.7991 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 7e9b3c8b-2cd7-3601-9593-1fd0a9f11379 | -5.52718 | -40.80293 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 17ac968c-dbc3-34a7-99ef-eebff048dc22 | -5.5265 | -40.79911 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 46a083c5-9c00-3108-9164-7b6e49c9279b | -5.5231 | -40.80386 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 9f9d7dcf-3074-38f9-b264-85e4972c4e7c | -5.52246 | -40.80005 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 7a56dccf-ec63-3156-a91b-a9eb11b78a0b | -5.52179 | -40.89745 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ebedb3ad-3d46-3fe5-ae17-633a36291d6d | -5.52095 | -40.89713 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ccad2df1-ab7c-3d0e-b6e8-839e086ad525 | -5.49711 | -40.71863 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 5c09832f-c9ba-3fc3-85dd-05f878bcf008 | -5.49495 | -40.71875 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 1deeae9d-5208-33af-b667-9fe7dfd69f99 | -5.48514 | -40.78359 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 65091596-0ce3-3fd9-a6dd-6e147f58a17f | -5.48448 | -40.77977 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 0aa55d39-f6e9-3a63-837e-a7a8698b0af2 | -5.48076 | -40.85826 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1752a9a2-c736-329d-9daa-c61cbe529bb3 | -5.4664 | -40.77517 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0c83d7ad-c061-3747-be7d-8ac32f11eebc | -5.46407 | -40.54546 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| a1a79143-523e-32a5-a656-d959f475176a | -5.4625 | -40.54983 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 242aa53e-a431-39c8-8366-9bf26acf2591 | -5.46182 | -40.54587 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b6f8faf0-ef04-306b-a698-0bce91e45259 | -5.46055 | -40.52576 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 4cbc4920-5f3c-3332-b0b9-ddbf4e7af964 | -5.45845 | -40.52611 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 26245718-a33f-3038-a5f6-140787db02fd | -5.4467 | -40.31512 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dbb2f275-8edd-3be5-a55f-f59f35176d59 | -5.44373 | -40.81038 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 76321f05-ce16-3210-837e-e314f3ea6e7d | -5.43093 | -40.83575 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| c5924c41-fed5-35e2-a4ed-dba83b56787a | -5.39063 | -40.70565 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9412674a-ba06-303e-b852-746a059ffaf8 | -5.38742 | -40.70718 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 66c7b22b-8c19-3ec8-b2da-1301953e67f1 | -5.38535 | -40.93043 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 56f96856-b693-3542-9fe5-8f70ab41f921 | -5.33058 | -40.87881 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1b0adbce-b6dc-3c45-a613-ce82981c2cda | -5.3249 | -40.87918 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7c79fd2a-7424-3ff4-ab88-17dc9705e2a9 | -5.2863 | -40.28859 | 2024-10-25 16:52:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 57892554-b40e-3108-9bfd-91c796417345 | -5.26753 | -40.48701 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 60b2f502-91fb-346e-8213-02e14d095386 | -5.25956 | -40.9907 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ae2ef521-554f-3c58-bdff-f78b452244ef | -5.25528 | -40.99886 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 51aae901-9a38-3620-8fca-5277b34b87c4 | -5.25466 | -40.99531 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 09f80287-e76b-3378-9223-875c6d162603 | -5.25406 | -40.99183 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 82966422-1c44-3c99-9fb2-9e514e4dcca3 | -5.25345 | -40.98833 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 882ebac9-60ca-3dc1-a3c9-fe087acaedc2 | -5.24977 | -40.9999 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 636dc1e3-945d-3a2f-a867-4d3f635bf151 | -5.24916 | -40.99641 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| be68cd9f-9e1d-32fd-8d4f-a46fe0106f57 | -5.23847 | -40.93528 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 123.7 |


[Clique aqui para ver as próximas entradas](README164.md)
