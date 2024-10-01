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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ec642cd-fa52-3091-b247-e29d141511b7 | -14.77141 | -48.78638 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5264d41-149b-3315-873f-0c758f58f39d | -14.76771 | -48.776 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00218e7c-5555-3965-b2d2-6cc14f7d6294 | -14.766 | -48.78443 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 977debd3-b5bd-3e01-b97e-531746fa2024 | -14.76507 | -48.78907 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bbcfcde-5166-3397-9bd4-164ec692e806 | -14.76044 | -48.78323 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4612bdfc-a2f8-3e6e-8fdc-fcb7c3ae548f | -14.75948 | -48.78798 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3b91a15-b54a-3000-8288-0e6ab35875fd | -14.7557 | -48.77801 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0f85507-755b-31f9-a659-b325ac47f2c7 | -14.75473 | -48.78277 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 209e5dec-cae9-307e-906a-3bdcf86be62f | -14.74524 | -48.77242 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 705da890-08c1-35ff-8bf2-790eebd9b487 | -14.74041 | -48.76762 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bbd9130e-00f0-3513-89eb-e11104932748 | -14.73953 | -48.77193 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27496dca-6e38-31f3-9c8c-e33da0a5dc2d | -14.73619 | -48.7599 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8bc66172-3219-3d33-a7ed-249572437742 | -14.73549 | -48.76332 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d499a0be-44a9-3c86-9329-1a17fa05eb6a | -14.7347 | -48.7672 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0a940f90-c80d-3be2-be9f-8340bd81f91b | -14.73249 | -48.74972 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c30ca9a-fc6e-3e42-a219-b9c063b59063 | -14.73177 | -48.75319 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0bc09250-53bc-3ba6-b517-42f0afca8d64 | -14.73107 | -48.75662 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b3fa2185-badd-374d-897a-02391a23089a | -14.73037 | -48.76002 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c26dfb72-c336-3599-8d15-82c827ecab0a | -14.72967 | -48.76345 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 674c93fb-c756-35d5-b0dc-e007cf5cf8ba | -14.72895 | -48.76694 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5a155d1-00ac-3331-bd67-4da52203b382 | -14.72823 | -48.7705 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 49d18205-8156-348f-83a5-f2df354e81cb | -14.72551 | -48.75544 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 159e3660-4b8e-33f5-a92c-bdccee3de064 | -14.72487 | -48.75858 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08e56b20-098a-3808-82af-80720f262f26 | -14.72423 | -48.7617 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5c9c258-bdf8-3b45-85e8-0ea580c1f5bd | -14.72352 | -48.76515 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 52dd0bad-0e4f-36ac-a785-27252264a626 | -14.72001 | -48.75401 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a0e608c-5220-3127-abbd-3b560d760d71 | -14.71939 | -48.757 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b983282-ba33-3ebb-aeae-e9c7b2827b99 | -17.5842 | -46.78053 | 2024-10-01 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4773ac47-23e1-3b48-8ea1-798c680a776e | -17.58107 | -46.7812 | 2024-10-01 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 400b4ae0-2667-3941-9fdd-88e137112765 | -17.57957 | -46.77952 | 2024-10-01 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd8bee5-da65-397d-94a4-599bc74268ba | -17.47629 | -47.00844 | 2024-10-01 03:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9689289c-a800-3fcf-9059-c0c72d89b1c3 | -17.26204 | -48.15264 | 2024-10-01 03:49:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 648c3596-82ba-36b9-89dc-a5c1c528c572 | -17.26141 | -48.15577 | 2024-10-01 03:49:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d596309-aca4-3654-8fbf-7f107338d51b | -16.51283 | -48.05417 | 2024-10-01 03:49:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bc7dd28-2718-3ffa-9967-3a8f561db9f7 | -16.51221 | -48.05721 | 2024-10-01 03:49:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b76aeecf-9578-377d-8b18-c21d235b3684 | -16.44839 | -47.00252 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 592986da-a1f0-38c4-9c20-9275334bf504 | -16.44723 | -46.99764 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd6d4da1-3d9f-392d-9eee-3d980c57cc35 | -16.44611 | -47.00323 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92603ee9-d052-36f6-b112-d61b3222eaa6 | -16.44354 | -47.00171 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1578b6eb-2f9e-3e59-a2fb-08ff3b1b867a | -16.43868 | -47.00098 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39612988-e777-3369-b5d1-81e8dc8a5e39 | -16.40054 | -46.86473 | 2024-10-01 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc36db8d-1690-33e9-9ed9-2515bd033b58 | -15.76774 | -47.71714 | 2024-10-01 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c50655a4-e119-3822-8b02-624ddc109f84 | -15.76715 | -47.72016 | 2024-10-01 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61b68340-747a-3486-a025-461c9ea0067c | -15.76264 | -47.71606 | 2024-10-01 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d23977e-26a9-343f-9b4e-112bdf5a6eca | -15.76206 | -47.71903 | 2024-10-01 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fad6978-1fc8-3d33-8062-6922cba32ccf | -15.56804 | -47.856 | 2024-10-01 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef7e6e23-c930-3238-a7f9-f347ab3a6815 | -15.38491 | -47.4362 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a31bc97c-3097-3ffa-9bbe-1dce0b089d4a | -15.38026 | -47.43316 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 355f4ec9-3986-3f4d-afed-672d59f90f82 | -15.37979 | -47.43554 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67c260fc-9d43-31c7-bc5c-b08424a1cefd | -15.37513 | -47.43254 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75b084d8-565d-3261-a838-a66406797cec | -15.36998 | -47.43202 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d92674dc-01f5-3e42-bd75-2e8df78616c7 | -15.36257 | -47.58931 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62dc0c0d-5633-3877-ace3-156701affdbf | -15.36194 | -47.5924 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cd132ba-2cff-3d33-b62c-658c5918f576 | -15.36054 | -47.58839 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 75313109-a51e-3134-9cb5-409b22524065 | -15.35993 | -47.59148 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d4d49c1-8af0-328a-a3df-9847c6342f8b | -15.35666 | -47.58104 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25847be0-d672-3df0-9f24-4209f4fbca1d | -15.35343 | -47.57042 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d666eca-487c-3fc2-ac3f-04c5213f693f | -15.35281 | -47.5736 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84a2fadd-befd-3589-a385-879524f8e943 | -15.35158 | -47.5799 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf7c83b8-7722-3f47-a14e-719656d86573 | -15.33138 | -47.54779 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e61a6298-5ddd-3fb6-a1a2-77254a97014a | -15.33071 | -47.55116 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4317d9-072c-32bf-86b8-661bc6bb0408 | -15.32633 | -47.5465 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144ceb06-81fb-3639-9d5c-472386758113 | -15.32568 | -47.54979 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f02cbc69-daf6-3798-ae1b-7b10a886ff8e | -15.29111 | -47.48436 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 619fd31f-f010-3e29-8cf7-8e8304fbb5d1 | -15.28854 | -47.48582 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8219170c-409b-3054-a903-08f9a3acd959 | -15.28803 | -47.48844 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c2118ad-8149-3edc-bac3-842663feb4d3 | -15.28752 | -47.49105 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d2a0c9a-bc1f-31a4-bd41-3b2ddbf729d7 | -15.28629 | -47.48205 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30f77486-d1b8-3ea9-92a0-968ed9fd1fd9 | -15.28523 | -47.5029 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9be302a8-8eb9-30e2-a851-f9f2aeac8701 | -15.28521 | -47.4874 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c60ef675-465b-37a5-9b8c-4f6080a00cab | -15.28467 | -47.49011 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 974fcc60-82d3-3e04-b97f-4d298f364bea | -15.28411 | -47.49287 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a01127c-5752-3107-8142-9f2ac868538f | -15.28352 | -47.49579 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e9dae08-ebaa-3e0c-b192-78114c2f7420 | -15.28289 | -47.49895 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f78110c-f7ca-3706-b12c-6e5ec33166aa | -15.28268 | -47.48885 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e05394b-b551-305c-84d1-fe54b4998d85 | -15.28224 | -47.50219 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f494fe43-ecd5-3210-ab37-dd75ecfb83cc | -15.28212 | -47.49172 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d1ca75-0439-3043-9795-2fd6ae4cd162 | -15.28161 | -47.50531 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57c48b47-99b4-3c1f-a58c-dfc03b5b903f | -15.28154 | -47.49471 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a33b43-b5e1-3aab-94ce-aab772605b6d | -15.28102 | -47.50824 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed862a39-2a02-3399-8d1a-4117a3e64c8c | -15.28093 | -47.49786 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52db6f0f-5139-3c03-8281-9f39d0433cce | -15.28033 | -47.50098 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e26b96b8-b9df-3173-88eb-791a917a147e | -15.27972 | -47.50412 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74abd351-8e32-3ac3-927d-7f1bb2dc6a55 | -15.20987 | -46.22808 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a8d1bfb-ffa1-3719-8309-46361b9f770d | -15.20526 | -46.22678 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c2861c-e4cc-335d-862c-0321203b669f | -15.20408 | -46.2246 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 609993a9-a97a-33a0-8a67-7dbc91d03944 | -15.20056 | -46.22591 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91f74d71-9759-3dbb-b74a-011f9978f00c | -15.19936 | -46.22387 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45a5d28b-e84d-3e6f-975c-8d21cc7b1a62 | -15.19847 | -46.22859 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e732a3c-c161-350c-a208-be49a1c5c113 | -15.19796 | -47.9519 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4120f63-c746-3b1b-98d3-18b9d0ff6c13 | -15.19731 | -47.9552 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 919cca1b-12e7-3461-9e03-000eea1c3172 | -15.19717 | -47.94946 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73d17915-9985-351e-98a3-2e12dca1b800 | -15.19651 | -47.95275 | 2024-10-01 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b04068e4-4546-3630-b30d-16cd6cdf2139 | -15.19583 | -46.22524 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47f64929-53f8-3d25-bf06-de3a8510717c | -15.19491 | -46.22994 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6081386-1620-3a9a-8246-7b7b037ed113 | -15.19398 | -46.23472 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c88f6c9-e040-32b7-ad0a-fed97d86e47a | -15.19374 | -46.22791 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c476e08-5de2-3b45-80d7-fe204865c76d | -15.19284 | -46.23269 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c193c7-3a86-3235-8b17-cf47aa3ce302 | -15.18922 | -46.23412 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51959f76-5026-3636-8c84-fa80f737830f | -15.18828 | -46.23892 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README48.md)
