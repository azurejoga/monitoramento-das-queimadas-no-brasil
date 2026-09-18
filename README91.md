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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d4ad6a-ee7f-3b87-a230-27c1e1ce133a | -8.4675 | -44.4984 | 2026-09-18 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| af008dfb-fca2-3fd6-b85c-e394e81ee786 | -13.4303 | -51.9036 | 2026-09-18 11:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6bfa2701-6237-3d3d-9bbc-f4e0d73caf93 | -11.2975 | -43.3851 | 2026-09-18 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 353.5 |
| 0b72086b-7280-37c2-ae93-f6250fc345df | -7.0164 | -44.6413 | 2026-09-18 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 9de8e9ae-6aef-3fa1-8496-0226477989f3 | -11.2783 | -43.388 | 2026-09-18 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 02f983c7-0be9-34ec-90d1-24dda53ff99e | -7.5494 | -45.6839 | 2026-09-18 11:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 185fa355-5c58-3f1f-9fd5-1ccec7ba6ff4 | -9.6019 | -45.855 | 2026-09-18 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 59934457-a59c-3e56-a948-20f879f405be | -10.6755 | -50.262 | 2026-09-18 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 101c9bbf-f2a8-35f3-b375-fcee3c50327b | -9.8316 | -48.3854 | 2026-09-18 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 394f4fdb-e8d0-3e81-8ba1-97a29f567906 | -11.083 | -48.2875 | 2026-09-18 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4ceada09-66d5-3820-b40b-cf4d14a025c6 | -13.6721 | -45.9898 | 2026-09-18 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 3d96e0b4-2f3a-3690-b3e7-e90870a0ba39 | -11.3167 | -43.3822 | 2026-09-18 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| dcc9aacc-22b3-383e-a363-4a99a3bce548 | -11.2979 | -43.3614 | 2026-09-18 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3ef717cc-d156-312c-9e80-585b44fbc4e6 | -11.064 | -48.2898 | 2026-09-18 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4aadf3b2-fae8-3dbe-8233-7aefea69ea03 | -9.8502 | -48.4053 | 2026-09-18 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 85352db3-95f6-3f91-b7ba-134d068f0e4c | -7.0161 | -44.6642 | 2026-09-18 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 382.2 |
| aec2790c-03d7-3dcb-b2b4-3759c929ffb7 | -11.2971 | -43.4088 | 2026-09-18 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| e2d652c1-ac99-3806-b81a-40193f7e56b2 | -12.6235 | -50.8953 | 2026-09-18 11:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 066f8676-be04-36ea-9e33-74fa6192f5cf | -11.8115 | -46.8158 | 2026-09-18 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9231b073-3975-3e4b-af80-46cf6a53b33d | -7.3546 | -44.6334 | 2026-09-18 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c2bb5c84-2dc1-3a9b-8f64-6c00494c9523 | -7.0352 | -44.6396 | 2026-09-18 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| c5ba212f-1357-3258-95c8-8f24ec6d5bf5 | -13.6725 | -45.9668 | 2026-09-18 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 628.9 |
| 0aa9413a-9ccb-36b0-a07d-d40b0ec01785 | -9.8505 | -48.3834 | 2026-09-18 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 034825e6-27e3-338e-abe5-7adb96d4b173 | -7.0164 | -44.6413 | 2026-09-18 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 260.6 |
| adda3cc8-4b5a-3ea7-976b-e49a7167f63a | -11.8115 | -46.8158 | 2026-09-18 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dd434480-291e-38a4-a387-38af2d22cd55 | -7.8027 | -44.9108 | 2026-09-18 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2f5b6839-6632-3d94-abf3-8a39d49e0e0b | -7.5494 | -45.6839 | 2026-09-18 12:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 64433b1d-c883-32e1-bbef-387521adfb3b | -10.6758 | -50.2406 | 2026-09-18 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 652f8bb8-0610-3713-8cbd-7a20b823471d | -9.8505 | -48.3834 | 2026-09-18 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| b571a8cc-531d-312f-a26f-90e0a3790505 | -10.5966 | -46.5474 | 2026-09-18 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6c84ba82-36f2-35c3-9b75-4fcb671afa2e | -10.1179 | -45.5662 | 2026-09-18 12:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e5d7df2d-2366-3a31-8d8b-a629f1348bc7 | -14.1732 | -45.1875 | 2026-09-18 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| ea4a1be6-74b9-360e-921e-2ff0c5c088f9 | -9.8316 | -48.3854 | 2026-09-18 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 9ab4f99a-8662-3683-9dc7-e14f0aaebc7e | -11.064 | -48.2898 | 2026-09-18 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d984d124-adff-3549-beb2-76cc40e22ddd | -11.3437 | -44.0141 | 2026-09-18 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| aca6fc28-ec6f-3eae-a901-48b96a68ff1f | -7.0352 | -44.6396 | 2026-09-18 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b0a56fa4-82ca-36ef-888a-9a8dc7bbcd6b | -7.0161 | -44.6642 | 2026-09-18 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 412.5 |
| 89703444-2063-3b0f-8ae1-df825ef6af77 | -13.4303 | -51.9036 | 2026-09-18 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6ac4ed78-97e3-3a3e-bb29-269d72bc9267 | -9.8502 | -48.4053 | 2026-09-18 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5c69a599-437b-355a-bfbc-0d83eab0e63e | -11.3442 | -43.9906 | 2026-09-18 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 07a66ee2-d0c3-35b2-915a-fec212b03da8 | -8.4675 | -44.4984 | 2026-09-18 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f792f852-88ff-36b4-ba96-9a8a9e79fcb8 | -13.6725 | -45.9668 | 2026-09-18 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| ec8bedf6-c938-312f-8b17-9ea3f013ba8a | -12.1527 | -46.9933 | 2026-09-18 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e885f854-1ad2-39d2-a01f-1028d8eb422f | -11.083 | -48.2875 | 2026-09-18 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 26dcd981-929e-3784-af57-273ed0ceb13e | -10.6533 | -50.4991 | 2026-09-18 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 06fc0031-048a-3dcd-a249-12913c27cd5d | -7.3546 | -44.6334 | 2026-09-18 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 646c2921-6100-369e-883d-3fd5a26b1fa1 | -11.0643 | -48.2678 | 2026-09-18 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2722d202-81c3-37aa-a6ce-e5e23158f0ce | -11.2975 | -43.3851 | 2026-09-18 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 5c50db98-db29-3b94-88f3-c37718d5b19e | -11.2971 | -43.4088 | 2026-09-18 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a9b2fcf5-d986-3309-afbf-24a3e227b6ff | -9.8502 | -48.4053 | 2026-09-18 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c85cd1a7-e40e-3f40-be82-91a867357e51 | -11.2971 | -43.4088 | 2026-09-18 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5fa9df8d-e7f3-33f4-af44-4ba01178e50f | -11.064 | -48.2898 | 2026-09-18 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b43be9cb-6cb4-300f-9916-85c8d850fa72 | -10.6758 | -50.2406 | 2026-09-18 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c82d7343-dd4b-3921-96dd-73806d530a70 | -9.8316 | -48.3854 | 2026-09-18 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 97b988f8-7a72-3883-9958-d678d9ea49ba | -11.3617 | -44.0817 | 2026-09-18 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f9406597-09ed-382a-82a8-3fdf8303aa56 | -11.2975 | -43.3851 | 2026-09-18 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.9 |
| f6576774-0ca6-3cc7-bc4d-d9cfbda58414 | -11.8115 | -46.8158 | 2026-09-18 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ecbaeb3c-ff26-3b62-9b6b-7c5e014782ef | -13.6531 | -45.97 | 2026-09-18 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fd4716de-85bf-3430-9034-ed7949f66ca1 | -8.4675 | -44.4984 | 2026-09-18 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 766f1a45-350f-36c3-b684-54da8efe5400 | -9.7308 | -46.1112 | 2026-09-18 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 48857beb-162e-3385-8220-cf00b83f382d | -9.8505 | -48.3834 | 2026-09-18 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 38533576-a9a9-3a43-9209-703b029e4203 | -11.083 | -48.2875 | 2026-09-18 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| af1dcd34-f7da-35d9-ab73-2c3faa4712b5 | -14.1732 | -45.1875 | 2026-09-18 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9623c686-ecc4-3e60-bb7d-7c97337abc2e | -7.0164 | -44.6413 | 2026-09-18 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 276.3 |
| ce362ada-a7cb-3c71-8a8c-5f93157045c8 | -12.1719 | -46.9906 | 2026-09-18 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6406998f-9e59-34df-bb91-e2886ad3bbdf | -10.6533 | -50.4991 | 2026-09-18 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 285c25fa-9739-335e-98a3-d95e38aa41a9 | -5.6285 | -44.7977 | 2026-09-18 12:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 23df3c38-4c61-395b-949b-921453a310e1 | -7.5494 | -45.6839 | 2026-09-18 12:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 88b0a379-7789-3f00-9a51-43057776e761 | -11.0643 | -48.2678 | 2026-09-18 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5ab55225-1500-3f81-93a8-34bab7c72ad4 | -7.0352 | -44.6396 | 2026-09-18 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| a668bb5d-cb75-352b-bf34-983da155a0d5 | -7.03 | -44.67 | 2026-09-18 12:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0c43100-18d3-3db0-bc36-1983e6e8e3c4 | -19.5539 | -47.6346 | 2026-09-18 12:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 2bbacba4-d846-3ec6-96e9-f6aed9c84605 | -7.0352 | -44.6396 | 2026-09-18 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 2f244e5c-0ec2-3ee3-9295-cf2e572dd1ad | -13.4303 | -51.9036 | 2026-09-18 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fbabbf13-2fc1-3aad-a2e6-19ef76174368 | -9.8502 | -48.4053 | 2026-09-18 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a11e0ac3-1b9c-30d1-b90b-a4ebf97b4e71 | -4.5774 | -42.9512 | 2026-09-18 12:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 2e8dd08b-f068-3225-a868-20d11165e17c | -19.5545 | -47.6113 | 2026-09-18 12:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 9171715b-701e-3759-b448-99f500603ff6 | -11.8115 | -46.8158 | 2026-09-18 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 228cc3a8-5d33-3876-afd4-7d2391f9cf57 | -8.6817 | -45.4359 | 2026-09-18 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d85bedcb-e57e-3d2f-ac80-6c042ef6e47d | -4.5772 | -42.9746 | 2026-09-18 12:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| bd394807-134d-38c7-8ba9-df716d0adebb | -13.6725 | -45.9668 | 2026-09-18 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 274.1 |
| f00cd617-4e21-3963-acf9-2e83dbaf45d4 | -7.3546 | -44.6334 | 2026-09-18 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 97887085-c6d6-3817-9a71-26f220f99bff | -10.3307 | -45.3112 | 2026-09-18 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ad759937-4bd2-37db-8a36-df1278096e09 | -8.4675 | -44.4984 | 2026-09-18 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 3bc67ab7-f31d-3ce7-a7d9-e40478160ccd | -9.8505 | -48.3834 | 2026-09-18 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 277427a0-f2b8-3205-b20d-f24df33457aa | -7.5494 | -45.6839 | 2026-09-18 12:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 98bc44d2-44d4-32ea-a6de-9b3ed94804c2 | -11.083 | -48.2875 | 2026-09-18 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2a1ea9f0-a598-3762-8dc6-76ae93aea243 | -11.2971 | -43.4088 | 2026-09-18 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3383e227-544e-3e30-9664-436ab7fe24c7 | -12.6235 | -50.8953 | 2026-09-18 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 83949814-6963-3db6-a562-21ab75e0009e | -10.6944 | -50.26 | 2026-09-18 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e8f482b7-7e8b-3adc-b4f8-57f58e0c974a | -8.4672 | -44.5214 | 2026-09-18 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b77b5fb7-8b87-3726-8bde-591b6d54f02d | -11.2975 | -43.3851 | 2026-09-18 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| bae65b7b-53b2-3cf6-8117-49da8cc672c0 | -10.6758 | -50.2406 | 2026-09-18 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0c7db8eb-ef2c-38ad-ae91-ea1a5dbafd92 | -10.5963 | -46.5699 | 2026-09-18 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1157643e-72c2-3168-bb3c-bd51e87735fd | -7.0164 | -44.6413 | 2026-09-18 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 275.5 |
| b3e08ec5-17a2-3735-8e46-d68b61290d00 | -10.8279 | -50.1815 | 2026-09-18 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| aad92289-d02f-3588-b7a3-5919fa098203 | -11.064 | -48.2898 | 2026-09-18 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4f1e705a-8f4c-347d-9fb0-61f201ec976f | -11.2979 | -43.3614 | 2026-09-18 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| b0973cab-2568-3717-bf1c-596a426f134d | -14.1732 | -45.1875 | 2026-09-18 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 73665880-ad66-3d83-ade0-89ee06b93cb8 | -9.8316 | -48.3854 | 2026-09-18 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |


[Clique aqui para ver as próximas entradas](README92.md)
