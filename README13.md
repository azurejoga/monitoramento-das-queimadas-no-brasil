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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c81f9af-9ee8-3ff3-a4eb-87a15288b362 | -5.91883 | -41.2916 | 2025-11-06 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ede97c8f-5fd5-3e7f-a4fe-7fa17ab794e9 | -4.71708 | -46.42811 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8cc6a3f9-4b24-3d4a-b00e-ee1fc313b6d3 | -6.28211 | -44.74558 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59bd9725-aed3-3377-ae01-f3791f6b226d | -6.99313 | -39.07278 | 2025-11-06 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc0a4462-997c-3d02-8c17-bbe3d3463275 | -6.27087 | -43.67897 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0fded8fb-8a6f-3762-8e23-73b68ef45d3a | -5.7695 | -40.83283 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 749eb530-c2a1-3d71-b063-c717e7f8f339 | -6.26201 | -43.68121 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ddcf6c19-7940-3dde-b7eb-153870f0ea91 | -5.76085 | -40.8195 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4baeae09-8018-3e82-9014-3217cdd6a1dc | -4.78675 | -45.13441 | 2025-11-06 03:53:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab5f144a-e3e5-3690-a015-7fd503ccbd53 | -6.12346 | -41.52742 | 2025-11-06 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b1bb7603-812e-3038-9399-90ed3186e983 | -5.42555 | -40.67234 | 2025-11-06 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a36c8278-933b-3413-a30d-e47d201a9ce8 | -5.83073 | -40.92366 | 2025-11-06 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67002470-657e-3e4e-bcfb-b709092d5d2f | -6.22748 | -37.42108 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 771d1660-5a4b-3907-afed-9a7b74d2b380 | -8.26526 | -41.92928 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 857063a2-8e7f-360c-ad49-aabefd093130 | -5.94618 | -44.26746 | 2025-11-06 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d552ed7e-1a69-3ce9-812b-5e884b642b12 | -5.24798 | -43.0064 | 2025-11-06 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1baae65-31ef-3c1f-a161-0bb3c5face9d | -5.29718 | -42.41722 | 2025-11-06 03:53:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 015508e8-19a7-33c2-86bc-3415c526cb0e | -5.08808 | -45.10173 | 2025-11-06 03:53:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c27827-a4fe-3edc-990a-b83a72402898 | -5.29637 | -42.42205 | 2025-11-06 03:53:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c28ebef-b66a-3b10-90f0-477f8549537c | -7.17852 | -38.35363 | 2025-11-06 03:53:00 | NOAA-20 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e7df183-07ce-3e93-b960-e4c404af08e6 | -5.46047 | -44.68697 | 2025-11-06 03:53:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45a4484e-c111-3e49-82e4-f901f7f8ec46 | -7.16796 | -40.08761 | 2025-11-06 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b12260a6-cf4d-397e-8eb9-79545ed54e0d | -4.78595 | -45.13924 | 2025-11-06 03:53:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3d724aa-e6fd-33df-8ef8-302beaa7585a | -5.75732 | -40.819 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d362d69e-a1dc-3a7b-8cfc-5d24c6e934a8 | -4.10877 | -48.02371 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5f00d7f-9d50-3525-b843-c6b72fa615b9 | -5.76634 | -40.80809 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f39dcbf3-5ddf-35a8-b451-0cac663d4b9e | -5.86067 | -44.37959 | 2025-11-06 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf9caaf7-c79b-3ed9-99ac-8430c784718f | -4.71946 | -46.4269 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2913acf5-166f-3f66-adb2-8eb85496808e | -6.20831 | -43.70758 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2f73e19-6bdd-3d8f-8176-6d177c3e03f8 | -6.44182 | -39.12089 | 2025-11-06 03:53:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41b5eb3a-6d73-3a1c-9510-caff1660b532 | -5.09031 | -45.43247 | 2025-11-06 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 160abec1-8d57-38e1-82c8-020fd688ef28 | -5.61063 | -45.0472 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c9d2018-ca94-3803-a285-f8c49531f7f9 | -5.75509 | -40.81062 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb37a103-819a-311d-9cc0-c99874cbf721 | -4.59616 | -46.5629 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbf70736-4329-39bb-b264-b684a0cc0305 | -4.87739 | -47.55264 | 2025-11-06 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947244ea-9b08-30ee-85d7-0f4ae5135088 | -5.31578 | -44.34373 | 2025-11-06 03:53:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40aec99f-47d6-3613-a971-8e0055b8352d | -5.09118 | -45.42724 | 2025-11-06 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 287d719f-0a7a-343f-b2c0-3c6eef996532 | -4.64261 | -46.32469 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b680453-fa04-3b04-a5d8-110f9c637787 | -4.37351 | -48.69721 | 2025-11-06 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3206eb4-71b7-312f-be37-cd947a02d592 | -7.0113 | -38.82999 | 2025-11-06 03:53:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2ade3f9b-7980-3497-ac06-df51d28d5def | -5.75444 | -40.81457 | 2025-11-06 03:53:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88718ad3-71a2-313b-965a-7c49a6a48ca8 | -4.21039 | -48.39989 | 2025-11-06 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e8f9f43-84ed-3790-9fde-cc2639650b5f | -5.24464 | -44.39017 | 2025-11-06 03:53:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 81b02532-c97c-3785-b72e-24b220f27aa1 | -6.27024 | -43.68266 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e2f7fb3d-b327-3ce0-856c-42bc42613b9e | -6.11495 | -41.55655 | 2025-11-06 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 187d0165-b43a-30bb-8ee3-ba15e69e98c3 | -4.69477 | -46.55622 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 834e4f34-6c9f-3fb4-a369-7df7fbd135ab | -6.97037 | -38.12242 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48d4eaf6-2ea6-3e6a-ad54-678d19a5c3d4 | -4.71229 | -46.43847 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f03896-4b92-3945-a26b-818d1673b2cf | -5.94841 | -44.26704 | 2025-11-06 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8bcc383-11a6-3d4e-a11d-c3f53ea7c164 | -5.39304 | -43.93849 | 2025-11-06 03:53:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46f864cf-ca0d-338c-9f45-cf6902277e28 | -8.04803 | -38.00738 | 2025-11-06 03:53:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e48169e8-b3b9-3200-bb0f-b73b6df49017 | -4.2039 | -48.40253 | 2025-11-06 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44a2e01b-5825-3f80-9c6e-387f04d08e36 | -6.98595 | -39.07517 | 2025-11-06 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15b06abd-67ae-3802-897e-4c6a38748b4d | -7.18128 | -38.35761 | 2025-11-06 03:53:00 | NOAA-20 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2e5cf41-df62-3647-aae6-538a82c876b0 | -5.77304 | -40.83325 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 694287c2-52a8-3602-b7bf-b090bc1326a2 | -8.32386 | -38.09001 | 2025-11-06 03:53:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1675c8f2-6cf8-30f7-9c26-b8b50e66d8fe | -5.7644 | -40.8199 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0feb79a1-a4d6-3947-9d5a-669816d0fc69 | -5.18229 | -44.93594 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a1d09b-b024-3387-8cbc-a93146df8744 | -4.71654 | -46.43121 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d26554c-df2b-3864-a1c9-b1e7a1155c9f | -6.76438 | -35.43263 | 2025-11-06 03:53:00 | NOAA-20 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be4cf3dd-2348-31fe-8c8a-ae748f3c6312 | -5.39729 | -43.93923 | 2025-11-06 03:53:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5164ac64-517a-3700-9bb8-d08fb24579d8 | -6.05055 | -44.15889 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54ae1332-8e55-396d-8389-1aa098713b23 | -6.2784 | -44.74053 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a8c284c-940c-3c07-be52-f17259848584 | -5.45971 | -44.69143 | 2025-11-06 03:53:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0b92df36-1222-3c8b-9fb7-de6fad8a2f05 | -5.61521 | -45.04788 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a8f1efa-c670-3548-a063-a9e61e027d61 | -5.75798 | -40.815 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 700470b3-00a6-3366-86da-9ca384e91e49 | -6.52128 | -38.7483 | 2025-11-06 03:53:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 294fb230-7f02-3ba5-87cc-b6b7cc2907cb | -6.70049 | -39.68776 | 2025-11-06 03:53:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9ae23f1-5b4a-3397-91fd-daf9ad5f53ed | -9.121 | -37.78871 | 2025-11-06 03:53:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1023e49d-c126-3559-a9c4-abd3cc941fdd | -4.69759 | -46.55865 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d8de68a-1e31-3271-930d-e2e06cc9045e | -5.76987 | -40.80858 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 982983be-10a7-30ed-9772-ac2127a33c3c | -5.24391 | -44.39453 | 2025-11-06 03:53:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b35b3b81-701a-37bf-8ed1-29f6aa0bce9e | -5.78913 | -43.04085 | 2025-11-06 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3fdda433-45cd-3a51-8a60-4656d4271b02 | -4.6013 | -46.56388 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3baa055-5707-30b2-a4c2-99259cbec761 | -5.18247 | -44.9331 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a916c0d-82b7-3f5d-9c6e-c1092ddaa6ef | -6.36551 | -43.75994 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a35e309-b538-3cc0-be27-b75a21d0bad5 | -5.41322 | -45.76173 | 2025-11-06 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f5d887d-2bdf-351b-8402-e649ea334f81 | -7.27956 | -39.38807 | 2025-11-06 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b489845-8296-3127-9f43-a8e390df5c53 | -4.10952 | -48.01945 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf0b7b95-82e3-3994-a51d-09ba32bbd1ec | -4.93193 | -45.72643 | 2025-11-06 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39c8cb88-cc0b-389e-96ce-39b4fd8541e2 | -9.12434 | -37.78926 | 2025-11-06 03:53:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5a82d663-9fc2-36cc-ad31-830a3ed3df42 | -6.05481 | -44.15963 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71584730-8a22-33c3-91d0-dbb2f12af871 | -4.71895 | -46.43002 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd4e73a5-4f09-3a6c-bd28-a335976fbb51 | -5.7546 | -40.81154 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 66aa2b9b-2d97-32f6-b528-a37fdf1bc3e7 | -6.30409 | -43.8095 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9f4e7fc-b0ba-374a-a49b-573a4c3122ce | -5.52728 | -46.50666 | 2025-11-06 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e14b6de-c3eb-3ce0-8e95-2ce00254d696 | -6.69861 | -38.20641 | 2025-11-06 03:53:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74451cc5-06c6-318f-9987-663df1b30206 | -4.64311 | -46.32181 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cca89065-2fc9-32bf-9068-b747d9ca0df9 | -6.27768 | -44.74484 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 782fcefa-568a-3248-98ec-93a0262a4690 | -8.32441 | -38.08651 | 2025-11-06 03:53:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee802295-ae11-32be-a32d-c030ab598ef3 | -7.73753 | -42.26336 | 2025-11-06 03:53:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4b886630-7f9c-36c1-8d17-93421c18419b | -7.006 | -39.33308 | 2025-11-06 03:53:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a74c17b0-d85d-314c-8bcc-9244ec8888b8 | -5.05112 | -44.65381 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38ceaf91-023a-3f2e-b345-e19a633ad76e | -5.86065 | -43.99688 | 2025-11-06 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f77696ed-1475-3416-ad84-a03169ecb84c | -6.98927 | -39.0757 | 2025-11-06 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c70f7f26-24ea-3711-b763-611574bc57a8 | -6.20417 | -43.70695 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13c07a27-3f0b-380f-ac07-c39a7763578d | -5.76662 | -40.82833 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb6fc5ed-095a-3828-abee-68ff1739b174 | -5.35351 | -44.92406 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97196ff0-da39-32af-923d-2c196542408a | -5.79228 | -40.80394 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f1f24a3-fe1c-3934-81ca-557d9e0c87d2 | -5.56486 | -45.09461 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
