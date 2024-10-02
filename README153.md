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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af9163f3-f98d-31c7-b29d-1377889f6796 | -16.78495 | -57.36829 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 65080be9-abb3-3568-9cc8-a4f8f0dc79ec | -16.78262 | -57.35979 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a233c61f-093a-389a-93dd-049a214843b2 | -16.78088 | -57.37173 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 00794c6e-16c2-3684-baca-62babc60d6fb | -16.77855 | -57.36321 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| aeed608c-175e-338e-9b61-6df02ddb6cd6 | -16.77739 | -57.37119 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| af784154-2dd0-3e6a-9cda-7cc94140b3e4 | -16.77508 | -57.4115 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 55bb6595-99d5-34e6-9e5e-0354476b4dec | -16.77218 | -57.40698 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 32a27de6-d03b-3725-8adb-2d13d10fa139 | -16.77044 | -57.41889 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cb0c825d-0c1a-3ee5-a477-68ad58fd9918 | -16.76984 | -57.37407 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 770c76d4-e8a5-30f9-bb8e-4c4dfccd0439 | -16.76696 | -57.41833 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 31100bb6-0836-3639-807b-cd29232b280f | -16.76693 | -57.36954 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| cfb78d7a-3148-3e2c-b07b-f0db4c81f00e | -16.76635 | -57.37352 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 416df176-48d2-32aa-81a1-79fe1a155bba | -16.76577 | -57.3775 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| a2d11c04-58c6-3909-bea8-f3970bcd1c70 | -16.76404 | -57.38943 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f17b894-3ea3-3bc3-a93e-b5ccb3779cb6 | -16.74428 | -57.37819 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| de70e38a-9270-35a3-86fd-62cfaa4eed74 | -16.7437 | -57.38217 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 81dcb23f-4ff7-35ff-ad48-d5730833374b | -16.7432 | -57.43486 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 61f62379-6a2f-3817-b61c-487b1a129a81 | -16.74136 | -57.37366 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b4f485bf-0062-3541-b925-ff0b91276632 | -16.74079 | -57.37764 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 81d06379-b779-3e6f-be7f-c56ed70fb3ab | -16.73972 | -57.43431 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1d0662a7-ce3f-3867-b29d-f73fb25f39fa | -16.73624 | -57.43376 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 79cf44c2-11d8-367c-a797-7a0cedc288bb | -16.73334 | -57.42925 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 24ad53ec-a265-3515-86f2-e708522721df | -16.72928 | -57.43266 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 88e1bd75-87bd-3c6f-919a-13b26a7c6c83 | -16.72752 | -57.42023 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6eb8ef69-72ac-3c8b-bd5c-f7caef3ac3ff | -16.72638 | -57.42815 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| e48d2e8c-1769-365e-9bcf-8cde8b8e0b08 | -16.72461 | -57.41571 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7bb9c176-b74e-3dc9-8f46-3922a69503a1 | -16.72404 | -57.41968 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| ed8fdb5c-6147-3f5b-bdf5-0febdb18a3a8 | -16.72264 | -57.41987 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 8909dbc3-8c41-3c1d-83bd-ec589aab4a76 | -16.72056 | -57.41912 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 8ce25a11-838e-355c-8ef1-93e5ff35a408 | -16.71999 | -57.4231 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 4700173e-fec5-332d-8fbd-b04fe62ddec8 | -16.71916 | -57.41932 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 30269c8e-9ef6-3551-bd7b-60a640945c29 | -16.71858 | -57.42328 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| a114a333-a212-325e-87ec-39efc8a6da4e | -16.70703 | -57.3809 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1327712c-65e7-3d57-bd33-43ab817db002 | -16.70354 | -57.38034 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7b030ae4-9932-35c5-b602-4ef4dc050c58 | -16.70241 | -57.33947 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0dfde801-64e6-3a5e-971d-2b93b38ab8c5 | -16.69601 | -57.33439 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d8fba2b7-284f-33b4-a165-75a4bb902a8d | -16.69136 | -57.34182 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5388b424-c27d-35c8-8e37-b6504d3f2e9a | -16.69019 | -57.34978 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c30b1033-018f-3dc0-9d3c-dabd272f906e | -16.69018 | -57.37418 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 861b10fa-584f-3ba9-bedc-40b57aa51907 | -16.68961 | -57.35376 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9282a589-254e-33b4-8bf3-283433e3dfa6 | -16.68903 | -57.35773 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3d94e7ec-be54-35ec-983b-a590bf9f0a2c | -16.68844 | -57.38609 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ff575f13-cd7d-3567-b0cf-15336e82b62f | -16.68612 | -57.37761 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9c01ade5-f607-3d65-83d5-ad024dd007ce | -16.68554 | -57.35719 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6da8f8c8-4251-39dc-a659-83dbb9663dbc | -16.68496 | -57.38554 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 324e3cbc-d1d1-3480-a60b-68df28e2f537 | -16.68438 | -57.36514 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 208b7393-3164-3346-ac9b-0530cf3e5979 | -16.65415 | -57.35226 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ea7435ff-8add-3cc5-8fbf-06aed04d73df | -16.65067 | -57.3517 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 483820d7-7c55-3c25-9302-a5937f325ff8 | -16.64718 | -57.35116 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 35776dfe-210b-3546-9c9f-9e574c901fb2 | -16.63319 | -57.32452 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f9d0f45e-6a49-33ee-873e-19b605e92845 | -16.6286 | -57.35636 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 40aba19f-7aef-381c-977c-d1f0d0ed6478 | -17.30647 | -57.46509 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| efbcdf66-f3e5-31f4-9d65-d550e70baaec | -17.21219 | -57.37372 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3efbeabb-fc6a-324a-ba92-10da1f59f6ad | -17.2116 | -57.37774 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6eee5970-e77a-3aeb-9d89-a68a3c1ca224 | -17.20868 | -57.37317 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1b32643e-952b-3f46-9d7f-274f19314b32 | -17.2081 | -57.37719 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c6197998-a4c7-307f-82d3-524655d194e5 | -17.20576 | -57.3686 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 28974d36-07a3-3599-b565-ca1df32c8a10 | -17.20518 | -57.37262 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e9cb76d8-c2b4-3c4b-927b-9ed858cfd325 | -17.20226 | -57.36804 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2252ad7a-40f0-3179-9354-7568e078d6b4 | -17.20168 | -57.37207 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 95acfdbd-9db1-3f58-ba61-1de3458a5f52 | -17.2011 | -57.37609 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b7edc11e-e4af-3233-b781-f4d4cc9e1f7d | -17.19818 | -57.37152 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6a53971d-f836-3e8a-aae3-63d1cc4d7c5a | -17.1976 | -57.37553 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8dbdb69c-915c-37ab-a19f-f8f37e3406d3 | -17.19644 | -57.38357 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1e7f9908-5170-3ca9-b85f-5554681d9960 | -17.19586 | -57.38758 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0828c97c-2b7c-3ff6-b94f-f4815495bd62 | -17.19352 | -57.379 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 17e53355-3dea-306f-be76-bce756b4e7a0 | -17.19294 | -57.38301 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4d1b3646-c151-3fda-a562-d35199a63b80 | -17.19236 | -57.38702 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c81da7e0-129d-3c89-aa1a-6d9a543b6ce4 | -17.18886 | -57.38647 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e29ccd3e-a953-3749-80bd-52b2c7d4fa4e | -17.10842 | -56.74766 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 100afd93-e85e-39d2-9c8e-89bf115b90a8 | -17.1072 | -56.75615 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 8b3b4c14-3b65-3a61-93e9-869d5bdaa8ab | -17.1066 | -56.76039 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 65225752-742e-3c26-9c08-76b936385f10 | -17.1024 | -56.76407 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| c19a6ecd-8ff6-3b4a-aba9-574453fc7e04 | -17.10002 | -56.75505 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 4d6f20f5-bd44-3415-aeef-b04e4495df88 | -17.09941 | -56.75928 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 41cdecd9-c7ff-389e-a4ff-3f4781e6be84 | -17.09881 | -56.76352 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| a404db32-8e24-3788-93a9-0d80a1317ca5 | -17.09764 | -56.74601 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1c678514-c0a8-3c90-9de9-cae95d04904a | -17.09703 | -56.75025 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b087876c-d387-370b-809f-ec728ed590d5 | -17.09643 | -56.75449 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5974409e-6aaa-3af3-b6f8-cb597141f199 | -17.09582 | -56.75874 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 18158dc9-38f9-3c68-a68b-f3a7fbd84e17 | -17.09522 | -56.76297 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 478899e3-4aa8-3520-b3ea-fba464fb084d | -17.09163 | -56.76242 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| c0c70b73-754a-33f4-92aa-b794f13be6cf | -17.08924 | -56.7534 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ba9c5fec-d855-3425-b351-c635a308bed3 | -17.08743 | -56.76612 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 0355c3c8-aa5f-3666-bf6c-247eaaf951d2 | -17.08445 | -56.76133 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 93073d6d-8b7e-3097-93a7-03823065b515 | -17.08384 | -56.76556 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 256cd874-6361-3376-b4a8-a8fc2c5a4137 | -17.08146 | -56.75653 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 78d86da9-4133-35ee-a0ff-ae7e15be6677 | -17.08086 | -56.76077 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4995190d-7d71-33c5-b8c0-4c071817e34f | -17.05812 | -56.76592 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 1cb8339f-bb27-3a09-bc56-9b3f452d08dd | -17.05753 | -56.77016 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| f955a671-9b54-31db-bbee-a81a9ea724e3 | -17.05603 | -58.03435 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| adbb98f5-3e4c-3f9f-b874-8ca656c2b486 | -17.05453 | -56.76537 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| dd1bed06-fe51-3b7e-beab-9fe4ea49c38f | -17.05262 | -58.03379 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d2ec6578-ba30-32b1-b6ca-66fd1e1f3b6a | -17.04855 | -56.75579 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ae5fbe7c-7cfc-331f-b645-4beabfe934cc | -17.04795 | -56.76003 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3293ebcf-2f98-3233-8d03-698585a2ca0e | -17.04555 | -56.75099 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9c27063a-4bd5-396a-8a23-f164af836e92 | -17.04255 | -56.7462 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 89dea6b9-fcf9-38ec-ad93-c977dc83f629 | -17.04196 | -56.75044 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9537b5d2-dd88-38bd-8ebd-a04287689a4a | -14.89505 | -58.03351 | 2024-10-02 05:12:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cf3cde4-edef-3c15-98f8-db1bcc4936ed | -14.84851 | -58.61723 | 2024-10-02 05:12:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README154.md)
