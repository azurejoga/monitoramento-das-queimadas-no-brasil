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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d853ccbd-9e6e-3d9d-8418-f56a3a600819 | -19.5772 | -53.51523 | 2026-01-09 05:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6da220ff-85fa-352e-9ef6-81c360255a87 | -4.2726 | -43.7832 | 2026-01-09 06:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 16c17cee-2218-3c0e-9bc8-717e9f283b08 | -4.2539 | -43.7843 | 2026-01-09 06:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ae691b9b-babc-398a-befc-8fcba288be9a | -4.2539 | -43.7843 | 2026-01-09 07:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ddedf4bc-8033-3e7c-a7d3-36b767b64852 | -4.2726 | -43.7832 | 2026-01-09 07:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 831005a9-fc94-3d4e-8a55-cd4c4174d02c | 2.55122 | -60.57793 | 2026-01-09 07:07:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c536eff1-87df-3b64-a471-f7c10723fdd8 | -4.2539 | -43.7843 | 2026-01-09 07:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| be928030-1ef0-39c5-b46c-5f1e656c046d | -4.2726 | -43.7832 | 2026-01-09 07:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| fd69b9ac-141b-381f-8a51-5b13225e41c1 | -4.2539 | -43.7843 | 2026-01-09 07:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9f0dcddf-32c8-38d9-81cb-881501946b53 | -4.2726 | -43.7832 | 2026-01-09 07:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| df700e68-98a5-3240-ae19-e25977acdb7e | -25.5856 | -49.8198 | 2026-01-09 11:50:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 159.1 |
| 378ec7a1-3a79-3764-b81d-8beffaa6192a | -4.92051 | -43.29757 | 2026-01-09 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 24d85670-7d55-3b05-9e87-a24418b6b306 | -3.87546 | -45.79945 | 2026-01-09 11:53:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 69f18025-5cb3-3666-9d7e-21f2c9ff2e46 | -5.00759 | -42.94126 | 2026-01-09 11:53:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 448dce97-3c2d-37fc-a541-dec158fa8bf6 | -4.82213 | -45.23814 | 2026-01-09 11:53:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fefa6921-8bc6-3903-b9db-377be2513938 | -5.54332 | -38.01529 | 2026-01-09 11:53:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| d41445c7-f669-3a1a-a0e0-72882b2d9125 | -4.36854 | -40.57026 | 2026-01-09 11:53:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f2d7cc3d-22e7-330b-8ffa-0f15a0c4e9df | -4.25168 | -43.77238 | 2026-01-09 11:53:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9914624c-e99c-3a84-b796-a2d0d82dccd5 | -2.69317 | -42.75148 | 2026-01-09 11:53:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7ca4a004-1fc1-3850-bd99-54d3579b8e39 | -3.33854 | -39.32497 | 2026-01-09 11:53:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 53.5 |
| e44c4273-8d85-3ca5-a61c-55c04809bded | -5.55182 | -39.63865 | 2026-01-09 11:53:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 13e4e9bc-46cf-37aa-93fe-ee51929e05db | -5.55354 | -39.62603 | 2026-01-09 11:53:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 816d4123-9e04-3637-b0d9-419f6eddfe5e | -5.54971 | -38.02184 | 2026-01-09 11:53:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| ff827144-e53c-308a-81ed-e8a17f95bf04 | -4.90781 | -38.9703 | 2026-01-09 11:53:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 105ecb06-bb2e-3bba-af09-61ef63cc9aa8 | -5.59428 | -39.99939 | 2026-01-09 11:53:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 21974ea8-026e-3d2a-aab3-8b98c82ea935 | -5.23269 | -42.20135 | 2026-01-09 11:53:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 2a7d66b6-7468-367c-8ee6-cefaa23b8645 | -5.54104 | -38.03185 | 2026-01-09 11:53:00 | TERRA_M-M | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 9ad78555-91af-3e5b-a2e5-67b2ce475831 | -4.92178 | -43.28877 | 2026-01-09 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66910026-0805-3d27-8ed1-ff6e0c113837 | -4.26815 | -43.78376 | 2026-01-09 11:53:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5c7e7a1b-6560-3b99-8163-4cd2f5e953a4 | -4.37286 | -40.56655 | 2026-01-09 11:53:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 466e8f23-c5ce-3b35-88a0-bfe4ab829c25 | -4.67083 | -42.39782 | 2026-01-09 11:53:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c4e62499-5585-3b28-a2db-e101433b866a | -3.34029 | -39.31268 | 2026-01-09 11:53:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 57419407-54a7-3011-be16-69398411401e | -6.89563 | -38.09449 | 2026-01-09 11:55:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 2cfe04da-d1ef-36d5-b1de-5701b5e5f650 | -6.89253 | -42.84505 | 2026-01-09 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7bef1fbd-693d-3ef6-9aa1-5c4cdac8bf30 | -7.05229 | -40.98869 | 2026-01-09 11:55:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5cc57bb9-541c-37af-9769-adec8926c89f | -5.73954 | -39.76477 | 2026-01-09 11:55:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 26.7 |
| c2be9e30-0399-3776-a6f1-2007c3e46f8b | -8.40936 | -44.04786 | 2026-01-09 11:55:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 40808d15-8f9c-31a5-89ee-aa4a87883d1b | -8.41063 | -44.039 | 2026-01-09 11:55:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1f308799-5eca-3807-b26c-b654603410e4 | -6.43937 | -38.3173 | 2026-01-09 11:55:00 | TERRA_M-M | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b3a87517-9aaa-35a1-a5e9-39722f9f5d94 | -5.59567 | -40.80222 | 2026-01-09 11:55:00 | TERRA_M-M | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a21e9b04-3fc2-3d1a-ad65-103c9eeae192 | -8.51837 | -43.28105 | 2026-01-09 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 1c2ff18b-8ba4-3a7c-8ec3-2ad539984534 | -7.6803 | -37.18803 | 2026-01-09 11:55:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 47.3 |
| dce17375-df8c-37d7-894a-5a13bc0dadb7 | -7.36241 | -40.81474 | 2026-01-09 11:55:00 | TERRA_M-M | FRANCISCO MACEDO | PIAUÍ | Brasil | 2204154 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f0b8fff8-cb5c-304b-8e21-344aa5809855 | -7.5106 | -38.80423 | 2026-01-09 11:55:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 33.2 |
| fc3deef2-7f2e-37b7-9067-918ce04b0487 | -8.5171 | -43.29008 | 2026-01-09 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 51108d02-e755-3221-ab66-e67f124e07ea | -5.74125 | -39.7523 | 2026-01-09 11:55:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 2108b7f3-ecb7-319e-a7f6-97001d193a3e | -7.68297 | -37.18281 | 2026-01-09 11:55:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 58.5 |
| cd425634-0e64-3a32-b6de-a51a2994a95e | -8.02068 | -38.40667 | 2026-01-09 11:55:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 087323e6-3caf-3534-8f30-f6d489d5d947 | -9.65089 | -42.95502 | 2026-01-09 11:57:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4b320188-ad2d-3d3f-a464-cb2619132c02 | -11.84785 | -43.70981 | 2026-01-09 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| def8bd23-106d-3664-82df-8556744e418a | -11.85649 | -43.71746 | 2026-01-09 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 39fc17e2-dad2-336a-a2ab-44e24e51df54 | -11.84655 | -43.71905 | 2026-01-09 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8526e3a3-b269-37b1-9f48-a70f48f53d17 | -16.73029 | -42.60453 | 2026-01-09 11:57:00 | TERRA_M-M | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e149bf5c-9091-33cb-8b38-7ee7899f4104 | -14.97119 | -48.8675 | 2026-01-09 11:57:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c96a7b45-5cf2-3d0f-bf73-d37cefa5531e | -25.57397 | -49.83841 | 2026-01-09 11:59:00 | TERRA_M-M | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| e5c6fdfe-c80d-377a-9475-e91e736ab8da | -21.23867 | -45.76311 | 2026-01-09 11:59:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7b395cee-574a-337e-b6f3-fa8c3b7c4f3b | -20.60215 | -41.20792 | 2026-01-09 11:59:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| f70fff30-f30e-30a7-8a9b-0b6a9d10700f | -20.73759 | -42.01568 | 2026-01-09 11:59:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 78a7894d-ccef-390b-be88-eab9bad9c565 | -25.39623 | -51.50209 | 2026-01-09 11:59:00 | TERRA_M-M | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 1fe93dc2-f914-3e88-9d77-1bf4434fc446 | -20.89349 | -42.34256 | 2026-01-09 11:59:00 | TERRA_M-M | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 272f732a-4f2a-3aee-9436-99fca46c542b | -22.46948 | -42.65348 | 2026-01-09 11:59:00 | TERRA_M-M | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 2b6bead6-b9cc-3eb8-b05d-ce83107c3f24 | -25.57563 | -49.82785 | 2026-01-09 11:59:00 | TERRA_M-M | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 145.9 |
| deb948ae-179c-3da4-9adc-1d819dbe6ac1 | -23.05912 | -44.92683 | 2026-01-09 11:59:00 | TERRA_M-M | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| bb050623-0d22-3fa1-aa97-dd18802c5dc5 | -25.5856 | -49.8198 | 2026-01-09 12:00:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 145.4 |
| 56f2cbb3-34c0-30fd-872c-51a5ebff5293 | -25.5856 | -49.8198 | 2026-01-09 12:10:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 122.8 |
| fa379d76-dffa-3f1f-999e-39b5cb5a420b | -25.5856 | -49.8198 | 2026-01-09 12:20:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| edccacb9-c9e0-34d9-b4f3-fd5c5673cecd | -25.5856 | -49.8198 | 2026-01-09 12:30:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.6 |
| abb5ff25-9d2a-3eba-9676-0173034639de | -25.5856 | -49.8198 | 2026-01-09 12:40:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 130.6 |
| a1bf5212-70f8-324f-884c-874e18668614 | -25.5856 | -49.8198 | 2026-01-09 12:50:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 117.4 |
| 4bfa5f8d-1ff1-3b01-b70d-b596004c7e13 | -4.3702 | -40.5731 | 2026-01-09 12:50:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 95.4 |
| b9fb52ec-078c-310e-bf20-f56d07a712a6 | -4.3702 | -40.5731 | 2026-01-09 13:10:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 85.2 |
| d9b07c08-7791-34ee-8908-8e1f10f7d4fc | -25.5856 | -49.8198 | 2026-01-09 13:30:00 | GOES-19 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |


