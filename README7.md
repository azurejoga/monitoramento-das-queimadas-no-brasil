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
| 81e66853-a32e-3e6c-9b66-ed58903ae3e7 | 1.51687 | -59.93314 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 746d1f0a-baf3-3ac1-a729-12d37981f684 | 1.49971 | -59.95065 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6abd3e24-d38d-3f30-b782-46c79bef463c | 1.47867 | -59.94686 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b983f373-c44c-3ce1-acc4-e67e68f55c72 | 1.94401 | -60.36475 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5320db12-38de-3f16-914d-6917108ae89f | 1.50362 | -59.93233 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 591fb6b2-51fe-37cd-86f2-707e174c9ae0 | 2.23749 | -60.70028 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c8c8730-e470-3d68-8a24-4011cb9ab7f4 | 3.05157 | -60.88604 | 2026-02-25 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fb23b3a-b125-3e0f-94a8-4dbb3d59f938 | 1.30668 | -60.40103 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 568c5819-c543-3eb6-bacb-d8e92e98121a | 1.31 | -60.40051 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a18f003-ac0b-3571-86ed-b268e4d14780 | 1.63404 | -60.28587 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 945b4dd2-4afc-3a4d-b791-057584c41178 | 3.43977 | -59.89277 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffc877e5-9ffb-311f-afbd-fe4bcc4607d9 | 3.13292 | -59.98622 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b183a69c-4eb5-3b76-b932-7dfe1c9d7eec | 1.92409 | -60.36786 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf9c4c70-742f-3893-bee2-a44d00010248 | 1.50303 | -59.95013 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 819090f9-5489-31ab-8272-c571e9175f4e | 1.51519 | -59.94402 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac22926d-a7c0-3988-8095-87b463eab434 | 1.93544 | -60.84349 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e533ea07-c16f-3500-aa80-e92e624ab1a0 | 1.49142 | -59.94132 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 808a5d92-7ff3-3b47-bcbe-bd2e1646e051 | 1.93296 | -60.35941 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69568c4f-8d49-376f-abac-18cb6bab2131 | 3.45325 | -59.89354 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ff52a22-4eef-369f-807e-5fd8bed93d91 | 1.50248 | -59.94666 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 22b689f6-1ca9-34a9-a647-2fc9071eb665 | 1.49087 | -59.93787 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| dd0ca29b-9980-3fd7-9373-667da006b0c4 | 1.3646 | -60.29662 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7b1a4f9b-1a37-3dc4-aae0-8a156097dfd4 | 1.51891 | -60.02905 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d3e9fe7-ac0a-343e-9b27-a35d9d16754e | 3.44254 | -59.88881 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cb922e8-b075-365e-937b-8b17b537d436 | 1.48919 | -59.94875 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 4717344a-ec13-3c84-8a3d-3c44b5d8c859 | 1.50417 | -59.93578 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 910dc55c-43a3-3b1d-a53e-88e30b9581e2 | 1.47703 | -59.93649 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cffc952f-0e08-3c6b-be1d-84ff125a97e6 | 1.76944 | -61.359 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a51d15a8-a361-3f5f-8782-7e4faeb8a0c9 | 1.94319 | -60.84938 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57a21b09-9bc2-3a8a-858e-f5285aef70b2 | 1.49861 | -59.94373 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5778a3f5-75eb-3328-806b-681dbcb00422 | 1.88482 | -60.91182 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdc80180-8ac0-3d79-8609-8d962560e0b9 | 1.5069 | -59.93471 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 321cd952-6af3-3c43-9970-0ea1b0cfdd6b | 1.93737 | -60.36579 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda3d0de-aaa7-3789-af02-2d28f89b5047 | 1.88094 | -60.90886 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26d4b72e-3776-3d16-9260-fd622d192dc8 | 3.44586 | -59.88829 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25cdfd6d-5a11-3bd7-939d-699744ed657e | 3.26554 | -59.92683 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 708291fd-ed73-3ae0-873a-225606c91522 | 1.48973 | -59.95221 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 7ac3a7a1-cd3d-38ae-a5e4-8ac1600c4846 | 1.49584 | -59.94771 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 10ffbd90-4561-3e7c-b529-716b2777dc1c | 3.45047 | -59.8975 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 660a4d6a-2c47-3de6-a1d2-6f0e12616584 | 2.71698 | -60.24593 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 266807a1-2886-3227-9921-d0f34954ed60 | 2.70757 | -60.25093 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a3b46c2-eee8-3682-a409-e4f45264e1bb | 1.50085 | -59.9363 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 244ca8ea-016e-3dff-890b-575703206733 | 1.94292 | -60.35786 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 953cf67a-e2bb-30bd-992a-c2016efa9a82 | 1.63349 | -60.28242 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29bd1020-3398-3b0f-9611-e34b599f7392 | 1.35679 | -60.05405 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbaf140d-a724-3ea1-9eae-f48e9f22709e | 1.93818 | -60.86082 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ad58c1a-cbb0-3ce6-ba9a-742632c71966 | 1.47757 | -59.93995 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45f9cbce-c91d-3efe-8cb0-322c37e9610b | 1.49697 | -59.93337 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5de19393-b097-3043-864e-60451dde5fff | 1.5046 | -59.9306 | 2026-02-25 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 393e96d7-db05-3909-b2bd-25a23ce52c21 | 1.4864 | -59.9498 | 2026-02-25 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 5d726a31-0db2-31e3-bdef-6de87acae959 | 1.4864 | -59.9308 | 2026-02-25 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 7089ddd2-83a7-35fa-9292-9c3d991fb489 | 1.5046 | -59.9497 | 2026-02-25 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 698262c7-90ce-3d8e-98db-abcea0a682f5 | 1.5046 | -59.9497 | 2026-02-25 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 1b5d6d80-fd19-3ea7-914f-ac0c587c0e7b | 1.5229 | -59.9305 | 2026-02-25 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d1291c44-93bd-3948-b5f1-4b299f3033f0 | 1.4864 | -59.9308 | 2026-02-25 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.8 |
| cc12b866-7874-3da7-ab93-ad739f357851 | 1.4864 | -59.9498 | 2026-02-25 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 3ed0c411-64ce-3e83-8d46-4dfe08b3dab5 | 1.5046 | -59.9306 | 2026-02-25 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 147.0 |
| be9b2333-a7da-3e55-9252-a6bb7c8933df | 1.5105 | -59.94197 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 567161ec-2c35-3ac4-a6be-4ec98dd4751d | 2.92938 | -61.40322 | 2026-02-25 05:54:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 801db77c-5e57-381b-9994-fdd1dea88aa4 | 3.05186 | -60.88392 | 2026-02-25 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068521c6-3605-374e-9616-40ed6fd9b562 | 1.94433 | -60.35991 | 2026-02-25 05:54:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed587189-86b9-3025-b7e6-5288b50fc0b9 | 3.25248 | -59.9212 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 208a51e9-d0b3-3a31-aeff-7197de337229 | 1.48386 | -59.95113 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 769c1191-4493-3c45-9a9b-96ea3fc12e1c | 1.50444 | -59.93362 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5ba3af2e-a7a4-3563-a9fc-4d2798280f6d | 1.509 | -59.93279 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f8d7868a-53c9-33c5-a560-d6ef8b62d4a1 | 1.49073 | -59.93587 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f67f6463-b6bd-3b15-96c5-6b6fcd810434 | 3.44757 | -59.90167 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3bdb0594-f11c-333d-8d45-3a15b7ea7074 | 3.13265 | -59.98841 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c77aed0-5167-346f-9cb6-84f1f4f32b7a | 1.48772 | -59.94666 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 7d98a674-bc23-3a4e-a888-cdab3fefab26 | 1.49529 | -59.93507 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 39f355b8-bfa8-3c34-9278-23d88acf4395 | 1.50137 | -59.91485 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3fe03c8-dd63-3887-927e-d8a662a5525f | 3.4498 | -59.88773 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f4a15a2-8d44-3c41-9894-d46937027fbc | 1.49376 | -59.95429 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ede8834a-ee1e-3755-9bca-a99d3413ea7d | 1.94504 | -60.8483 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b35b55-dee4-3d62-a8ac-6aa9577e9cf3 | 1.31105 | -60.40117 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23d0ef0b-8dfc-3a9d-9e86-19c7f8b89fb7 | 1.51593 | -59.91772 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e289dcf5-10ff-33d3-be63-d3f4e09d4431 | 3.51497 | -60.38454 | 2026-02-25 05:54:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f6a86c1-9f57-3033-aa2e-7935fec063c5 | 1.50974 | -59.93735 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7639b4eb-4d76-3cc9-b29e-c97685e15d97 | 1.51202 | -59.95127 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dafc41b-4e0f-3a01-8a89-d36b371c5b97 | 1.50669 | -59.94735 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60acb440-13eb-3fae-9bc1-e12f6f374750 | 1.50593 | -59.94273 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 324d3ce7-85f0-388b-8b34-745892bd74ec | 1.88585 | -60.91482 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b37cc67-813e-3263-bf63-1a619d599e70 | 1.48463 | -59.95582 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| cd6d9e97-9545-35c3-bb88-76eb6a18615a | 1.2061 | -60.62013 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb985e34-bf97-3951-9bd7-a9892e491ce4 | 2.71174 | -60.22645 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1394748-e7c2-3fc8-a39c-cf55ba37eafd | 3.24803 | -59.92192 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16b718cf-88ec-33f1-9ec9-b2fd5b0ec229 | 1.48182 | -59.90907 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ab75de4-9f45-3d97-b5bc-c78d03ebb98b | 1.51666 | -59.92219 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e16b42dc-2b17-3368-b782-2da6383c515e | 2.71516 | -60.24786 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 431165b6-0229-3070-811c-965c78079595 | 1.49086 | -59.93681 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b910c875-556c-396e-8cec-7c6faa94ab8c | 1.50136 | -59.94349 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e7a330d3-60c8-34c9-a93c-0486b901ffea | 1.48845 | -59.95133 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f50e9338-80a5-3e86-af03-07f953b05d49 | 1.51125 | -59.9466 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3e541da2-9554-35c8-9bdd-c0ad9bb2c4b0 | 1.49452 | -59.93039 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49328650-a8b1-304d-b557-44c9cc3628d9 | 1.48917 | -59.92641 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6ee312f-0e9a-342a-9150-700b60d9155d | 1.94077 | -60.84897 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3c14861-df8b-3016-815f-0510252bdea4 | 1.51739 | -59.92667 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c7a6e26-616f-3087-84eb-896cf46dbff5 | 1.51355 | -59.93195 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 201bd162-6aa3-33cc-9a00-345d44f2b9a0 | 2.71614 | -60.22573 | 2026-02-25 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ab2a68-934b-3cce-a7f8-7ea52d0440d1 | 1.48406 | -59.92335 | 2026-02-25 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
