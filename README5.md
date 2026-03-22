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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1582194c-3e61-3523-b836-0ee7d6c385e2 | 1.04622 | -60.36225 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83eab538-1065-3008-a044-1dc827c1a822 | 1.15847 | -60.33077 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b31fe2c8-146e-33bf-8905-47e9bb0c0bb3 | 3.27336 | -61.19644 | 2026-03-22 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb71358-ba23-384e-aeb0-48b59a6e7c49 | 0.98576 | -59.38887 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e17b2833-249c-3091-bcbf-1259835a2555 | 3.92304 | -60.93525 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98b70242-82a8-31d5-9324-0a92e3a2a97c | 2.64883 | -61.29502 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3fd0f274-723e-301b-b0ac-dfe850881da4 | 0.54322 | -60.26353 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b99f7edc-f022-379c-8e7f-c37beb3d4928 | 2.64661 | -61.30241 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d5c36856-72b4-3834-a35f-1ba97d8b1c36 | 2.64991 | -61.30189 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6b077887-57b5-37a3-b1a7-c4d3edd30ef6 | 1.21373 | -59.97242 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc632138-6ddd-35a7-be61-6ee0203747ad | 2.59613 | -60.59277 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aaaeb15-0de4-3788-bebb-ee556ff8b027 | 2.64445 | -61.28867 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b34fd8a1-69bf-3695-b6bc-9dd2193173e5 | 2.03841 | -61.26799 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b37121-b9b1-3768-a394-1353f33d11a8 | 2.65489 | -61.29056 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 365b4863-bcfb-31ba-ab48-53866d187824 | 2.39453 | -60.39619 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d603d615-8685-3e4a-8bab-7ba956d97336 | 2.25112 | -60.28692 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 828ab7e7-a84b-32c5-aee2-980e2d0e02e0 | 3.24042 | -60.29992 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e68e11-2b0b-32f5-9593-db612f99b3ed | 1.72104 | -61.17637 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd954c33-98df-3fbb-bfe4-010fb3659667 | 3.9093 | -60.93386 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b911fbd0-8494-315f-8521-6636fba5314b | 1.89667 | -60.62648 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e622c4-a62a-318a-8532-353c5afe84bc | 2.05209 | -61.80701 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 587b9b49-cdd2-382d-8fad-78c1a4263004 | 2.64331 | -61.30292 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1b6daf08-52e6-3035-a7f3-af7eb6b3b714 | 3.23241 | -61.19935 | 2026-03-22 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b92a219e-627c-3724-a7e6-fce9d40850c4 | 2.64721 | -61.28471 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 07c9d795-19bf-3dbb-9a68-7a66efdb2a91 | 0.61385 | -59.86304 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21743e48-eea0-3bc5-a514-777e20240fa9 | 1.12353 | -60.18251 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 805c51b8-55fc-30c5-a0e7-5efe2fec28ff | 2.65105 | -61.28764 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 22272f05-2d92-370d-aa98-e5f727a0236b | 2.65435 | -61.28712 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c46cd71-164a-3553-a430-e0d0f0344121 | 2.64607 | -61.29897 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c834ebca-e0ae-3cbd-8f91-e5411bbd24c1 | 0.85998 | -60.24586 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1b7ace5-fa64-3923-87c6-41460b4bad0b | 2.05967 | -60.21373 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f33ad37e-b814-3151-aca1-22dc5b0f20f3 | 0.93225 | -59.5055 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09208c16-2c0f-3e55-bb07-ee7a51424eb0 | 0.98928 | -59.38832 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56a78d12-d1d7-31fd-9318-0da58323e212 | 2.65375 | -61.30481 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 80e8ebd6-5094-3e05-8268-c239a39c763c | 1.27698 | -60.10643 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59f3e6b1-8371-3c8c-8d4c-374424f08c7b | 3.57629 | -61.73856 | 2026-03-22 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5ee6555-8bc3-3e23-b1c7-4316a5c62fb8 | 0.98867 | -59.38438 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 532f3af1-7c1a-3cda-bada-adfa4d17cfe9 | 2.11986 | -61.22287 | 2026-03-22 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ea67107f-2a81-3046-91de-3e427007d2b8 | 1.34565 | -60.02845 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36c4620-9149-3d2b-915c-a03e484e85d0 | 2.64937 | -61.29846 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ae01f929-de79-357c-84cf-ac02d27158ce | 1.67781 | -60.3131 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcc1e152-816b-345e-9bbe-5ae728b4ead7 | 2.64001 | -61.30343 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e6103b2-da7e-3b20-b26d-fc122cc614a2 | 1.08364 | -60.34939 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc85bad3-5f08-3496-99b7-b7ea0fe52e73 | 3.23187 | -61.19591 | 2026-03-22 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20bbdb63-fb4b-3a7d-acc5-db0955a1f807 | 0.82019 | -60.50836 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff59b3c3-b043-321e-b1c3-044bc7733aba | 1.86251 | -60.45374 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869de675-ea97-3fd0-bdb0-1d56404cc002 | 2.64775 | -61.28816 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 61338872-88a0-3e9c-9cfe-72de710a5ba1 | 0.63907 | -60.00194 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e543e2-3084-3f6a-a205-6685546c1332 | 0.98515 | -59.38494 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4c8c0400-035e-3be8-898f-bf0a9496767c | 2.65267 | -61.29794 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6000e7c7-f48f-3f37-a20c-c11403fd9856 | 1.25274 | -60.44551 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 345aabf9-6e8c-3712-94f5-e8523c6d95e7 | 0.99218 | -59.38383 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f1593ce7-d197-3428-a33c-1f440f1b0ffe | 0.93825 | -60.50135 | 2026-03-22 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91c453cc-94a9-3e44-b7f8-44c7161f3054 | 1.12013 | -60.18304 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2acc7095-4de1-3886-b027-e028263a0ad6 | 2.59279 | -60.59328 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea02a92b-26b1-3bc0-964f-269855f5fc19 | 2.59237 | -59.96367 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88c9082c-baa3-37f7-be1e-f1636bb749f5 | 1.20524 | -60.62517 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c4b11c-f9f0-380c-a6f6-5c0980f5a897 | 2.59001 | -60.59732 | 2026-03-22 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9de1cf26-e165-3816-b743-f06a4a433795 | 2.64715 | -61.30584 | 2026-03-22 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0c216d84-4b76-3f32-9623-effe2d2f2524 | 1.08419 | -59.73098 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed6f8473-d0b3-324b-a396-07c4ec1bee96 | 0.98744 | -59.3765 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26dfe5f9-911f-30f7-9038-451a2e7c7723 | 0.98454 | -59.381 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a9bd7d09-4efc-3fd6-8c43-86e58d21e980 | 0.98805 | -59.38045 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0e432b93-68ad-3adc-9d87-eee9b203d2c1 | 1.2533 | -60.44911 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa38540-c4c6-3b5b-bfcc-9355d28fc1e7 | 0.57143 | -59.90847 | 2026-03-22 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d615492-cd4d-3020-ac68-3bec004f040a | 1.72632 | -61.16441 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e361a736-b57f-312e-ae9f-b02dd5d4a015 | 1.64459 | -60.2998 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ec697e3-f8f3-32b2-843a-147a224b35e3 | 1.16186 | -60.33025 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cea4494-22b7-370c-ac73-47e00d4d4ad2 | 1.63275 | -60.29053 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05057596-b3b7-3fc9-8797-363cebce9e99 | 1.08359 | -59.72719 | 2026-03-22 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf0fbfd3-efd5-35c6-99b7-619af41a1b6a | 1.72963 | -61.16389 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d568592c-279f-32ff-8f32-d2fb658e9344 | 1.54548 | -60.20779 | 2026-03-22 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0719bb3-8485-3789-b10a-3d81d4792807 | 3.24098 | -60.30345 | 2026-03-22 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8925e42-29b3-3221-ae7b-27165e9b0b19 | 0.52618 | -60.26618 | 2026-03-22 05:36:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f342fce7-a3ce-3b2c-aee3-39196f22166c | 0.51537 | -60.26411 | 2026-03-22 05:36:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67fd13bd-3374-38a8-9d95-b3d1938641fc | -1.55735 | -54.0099 | 2026-03-22 05:36:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1537a7af-5d2c-3bcc-b8bb-e54cd641d606 | -1.55782 | -54.00678 | 2026-03-22 05:36:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b0063c0-a1f9-3919-9921-d100c51cb28d | -9.04544 | -63.33134 | 2026-03-22 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8d2fad3-b489-3146-a95f-c777d098abab | -9.04877 | -63.33186 | 2026-03-22 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfb96718-57af-3b41-8e52-a5db915afdde | -7.98482 | -63.68139 | 2026-03-22 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcefb6de-434e-32d7-a780-6f76c5d393ba | -9.04598 | -63.3278 | 2026-03-22 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85d97544-2034-3e16-95c0-ae8a89f27d7b | 2.64769 | -61.2863 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 405c10ce-3efe-30d0-8a76-ff6190654033 | 2.6409 | -61.30145 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d872faf3-042b-3c03-9ec8-ac8b9e4266ec | 2.64317 | -61.28702 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62b73c34-3ff5-3df8-80d0-6f19899c6c57 | 2.58948 | -60.60009 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07807bcc-c4ca-307d-a4e4-3e27b9765644 | 2.64844 | -61.29085 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0c696009-34e9-3329-a0e0-7d0761693e9e | 2.64993 | -61.29996 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3c58249c-77e9-3a9e-9cce-a93db84acdd7 | 2.65221 | -61.28552 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cbf3f28b-f37c-3e65-a79c-5f1e4937a2b1 | 2.64392 | -61.29161 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca21081f-c4a8-3f4b-90ab-60fa9a2e5dc7 | 2.64165 | -61.30602 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5bbea79f-08b4-341b-bbfa-6914ab490a6f | 2.24884 | -60.28751 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfca2b95-9914-31db-9a74-dc7fb44ffbac | 3.57646 | -61.742 | 2026-03-22 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 205ebec2-bb65-3a4d-a3fe-7d762374f654 | 2.65294 | -61.29002 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 25227cf3-aad0-34cc-8c67-44fe0ea328f8 | 2.64467 | -61.29617 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34416ffe-1ef9-3c83-8e80-49f6291a3b8c | 2.65519 | -61.30374 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 15ec1430-552f-3b40-85dc-86c360987067 | 2.59303 | -60.59593 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5bb752f-1610-3e8d-9d5e-54652d213259 | 3.24468 | -60.30282 | 2026-03-22 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0972e652-417a-33f0-9f1a-0ad33a5693f0 | 2.59338 | -60.59425 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f6c3326-96f4-3f48-ba3f-6fb969661258 | 2.3334 | -60.38678 | 2026-03-22 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c952be23-cb9a-335a-a477-467f7bb64ca4 | 2.64542 | -61.30075 | 2026-03-22 06:03:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README6.md)
