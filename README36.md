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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 672550c8-102b-3df5-bf06-a293f761a980 | -2.79472 | -53.98884 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f98dd813-e48d-3ff3-aeec-6a98840746a8 | -2.78897 | -53.98009 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f03b0c6-04c0-3430-a437-4d368af01b02 | -2.78576 | -54.02282 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68736063-8329-3148-94fa-0ec91384c343 | -2.78515 | -54.02665 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5566b96d-f602-3de6-a916-a4036eff039c | -2.71137 | -53.98866 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09b1fdee-7b22-3687-a73b-147dd2cbe01d | -2.71077 | -53.99248 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c7882a1-f06e-3198-841c-a6ae65e12194 | -3.31455 | -54.12268 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cc64256-75b5-3ec6-8fb2-f0fc6ea4c0b0 | -3.2698 | -54.17866 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6be701f2-c6aa-3ce6-a617-7bba079fc6c1 | -3.26919 | -54.18251 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c98467f-1ccd-32a0-a184-f6cc4f9fe526 | -3.16154 | -54.92051 | 2024-10-19 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 613e7577-2dc3-39e4-89b2-89994b0f62fa | -3.16087 | -54.92465 | 2024-10-19 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99ab00d8-2e93-3843-a4ac-1b05a29cce87 | -3.15792 | -54.91992 | 2024-10-19 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c86647d2-5bce-3cf8-840c-6d4402e92dc3 | -3.14936 | -54.25594 | 2024-10-19 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5522fd44-6368-3b33-bd87-4f14b74b83ec | -3.1491 | -53.98052 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85ec6595-a86d-3830-9513-839224aa9543 | -3.14874 | -54.2598 | 2024-10-19 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dae82d34-b169-3cc4-88a3-36d55ca81ab5 | -3.12218 | -53.74832 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dda3d75-d3f0-35de-b459-e7c2452c46a7 | -3.11933 | -53.74405 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18d617be-0f38-3e28-87ec-cfa334e082ea | -3.11873 | -53.74778 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4787dc1-92d8-387b-a79d-2bab1c556781 | -3.11304 | -54.99006 | 2024-10-19 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33d72f29-0457-3313-83d5-2a67edc53645 | -4.44464 | -55.41107 | 2024-10-19 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2584ba4c-46b5-3f5c-9c48-f3729d75d888 | -4.44379 | -55.41361 | 2024-10-19 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1394a38-ba27-3650-8379-f57702a3013c | -4.32632 | -55.42928 | 2024-10-19 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594d99e7-eb75-3f4b-b4b7-99d4a8f2ab6d | -4.25477 | -54.67163 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3072c2fa-04d7-36b9-8690-cd6ea6d31dcd | -4.12802 | -54.89962 | 2024-10-19 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4b09626-ddbc-3d58-9c69-137077a2f26a | -4.05165 | -53.87603 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0685cc8-f51c-31d7-a6b5-5070fffc1cec | -4.02978 | -53.9678 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0057252f-5338-3ed6-a4ea-04293329b70d | -4.02917 | -53.97153 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea66ad12-6341-340c-a50d-6e12dafb3969 | -4.01585 | -54.36352 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f08d64-1fbd-39d7-935c-216b9eb2f757 | -3.99591 | -54.19883 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a397c10-e1a8-3aae-8818-7be470092bbf | -3.93215 | -54.72579 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd4d0f94-2372-37ba-9d0c-04d1e38aada1 | -3.86481 | -54.2225 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abb3d113-ec67-3823-b26e-c6838e0cc565 | -3.62697 | -54.67152 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c00acd55-3b1f-3cff-bd16-3d99e4d00e3e | -3.6234 | -54.67097 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80221e10-b21d-3690-bf3e-46626a22cae6 | -3.62049 | -54.6664 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41135469-a017-3ba4-81ef-ec8e2a207c8c | -4.05449 | -53.88026 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80a89cc8-5743-3e3f-a504-99cea61dc807 | -3.97602 | -53.97834 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02610ede-753d-3efb-bc91-755d12aa6309 | -3.85883 | -54.08075 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0023285f-cbdf-364b-813f-a0ccf84fa709 | -3.83102 | -54.23275 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2edb6bf-f220-3e8d-8062-4762bbaac97a | -3.82759 | -54.61119 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0702e48-cb7b-36a5-8298-3b70f205e243 | -3.68689 | -54.21019 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67ac4527-a040-3b3e-b15e-ad37783a8ff4 | -3.68627 | -54.21403 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f9432d9-bccd-35f3-9a36-963d63755d2f | -3.68455 | -54.56207 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59f13fc2-4535-3184-9d35-ab9986cf01ea | -3.68392 | -54.56602 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38378610-8ab2-30bb-9a2d-3714fa933398 | -2.06081 | -55.86308 | 2024-10-19 04:49:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c6f0c86-5118-39fa-a9a7-b5cd8c784a61 | -1.85109 | -56.37261 | 2024-10-19 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 466ec19a-7b32-39f6-bde4-7c50a8086d0f | -1.85053 | -56.37608 | 2024-10-19 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e800acb9-71b7-3b60-8384-3f29fc3b0981 | -2.47272 | -55.62327 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f895d1-0b36-3e9c-8362-3ea28225312a | -4.50976 | -55.83092 | 2024-10-19 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3efa091a-88c9-30cd-a535-796ece06f9e3 | -4.14539 | -56.09795 | 2024-10-19 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce733466-fd33-3cbf-9b8b-c73a403169d1 | -4.14462 | -56.10265 | 2024-10-19 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4beed086-b39f-34f5-8e17-dc3f264b84a5 | -2.94047 | -56.82893 | 2024-10-19 04:49:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca7d53d3-5de8-36a0-a62e-af2aa4a4e84a | -3.0838 | -57.32302 | 2024-10-19 04:49:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| add62e24-85b8-3a79-9076-79bdfb9e7066 | -3.08317 | -57.32686 | 2024-10-19 04:49:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc499129-4c18-30a5-b0fc-a6334faee81c | -2.41056 | -57.89595 | 2024-10-19 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bee13c1-dd24-39e8-ba5a-68f4df79aa0e | -2.40988 | -57.90025 | 2024-10-19 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2df102-5ecc-36ed-8bfc-18c517599f8e | -2.37707 | -57.18106 | 2024-10-19 04:49:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da3ba2ca-572c-389d-872a-2f6e8cd689a6 | -3.21306 | -59.35524 | 2024-10-19 04:49:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70da8b3b-6301-3068-8bc2-3867e301224a | -3.2122 | -59.36048 | 2024-10-19 04:49:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b82078-402a-373c-a78f-f78884d3ceb3 | -3.06866 | -59.18957 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4de7c983-b18a-3cfe-80c9-86d758187e69 | -3.06862 | -59.1936 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9da0ae3-d338-3ff7-89bc-736fb652d0d2 | -3.06779 | -59.19472 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 651311ad-69e9-3a0f-9f1a-a0d9c13ebbbb | -3.06389 | -59.18879 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e933a10-0c86-32e9-8ce0-da19fb570b3f | -3.06385 | -59.19279 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5b71535-c9c4-300c-92b5-95a7df911ce9 | -3.06302 | -59.19393 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d391ade-894a-3ba7-bf84-5453ef0283cc | -3.05991 | -59.18684 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 703e818c-c6aa-36bd-9782-53728ab33516 | -3.05913 | -59.18799 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95f2d212-955f-3b22-98e8-a08922cccaca | -3.05908 | -59.19198 | 2024-10-19 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 333be1eb-8870-371f-970c-e32538e76816 | -4.26978 | -59.99293 | 2024-10-19 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e83d545b-195c-3dca-860a-399aa831258b | -3.98964 | -59.21435 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc9c7081-996a-3554-94c1-aeaad7263d06 | -3.98882 | -59.21933 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00783774-34e1-383e-863a-db9a5a1e7818 | -3.98798 | -59.22436 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b7f2a23-75ec-3600-92c9-9d25202f677b | 0.99706 | -59.44627 | 2024-10-19 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9f3311c-57f9-3470-976c-5fe4f4bd3073 | 0.99659 | -59.44324 | 2024-10-19 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3d2edd-3527-36b3-9153-6433ef6655ff | 0.99613 | -59.44023 | 2024-10-19 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d808fe8e-5fe3-31de-8634-e92266320dfb | 0.99189 | -59.44715 | 2024-10-19 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79982e38-d4a5-38ea-82eb-4181d54f1f88 | -3.27836 | -60.23168 | 2024-10-19 04:49:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56c83aef-d72d-318b-8b3f-e1c55cd50c73 | -3.27787 | -60.23467 | 2024-10-19 04:49:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1859974b-47ba-3e93-956e-f1979b33e67e | -4.50904 | -61.11153 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4efabfe-ff81-32e2-accc-1f03c4640fee | -4.50848 | -61.11483 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a991768-cd82-3baa-9313-2c32c82923c0 | -4.50791 | -61.11813 | 2024-10-19 04:49:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a999c0c1-d220-3c49-9194-d776f51443f3 | -3.99709 | -60.39666 | 2024-10-19 04:49:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0489a62b-c3d5-393a-abe8-b0bd53868205 | -3.99659 | -60.39966 | 2024-10-19 04:49:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb084316-900f-3645-9f4d-e77070489d5f | -3.99199 | -60.39578 | 2024-10-19 04:49:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1ed14d3-3068-3af7-98f4-ae618896ba5d | -3.05521 | -61.67585 | 2024-10-19 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d08608-60e1-3163-9a35-5fd8d1deabda | -3.05458 | -61.67968 | 2024-10-19 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72d7f0cd-bf6f-3026-a2c3-c3f08fd885ba | -8.57289 | -49.22161 | 2024-10-19 04:51:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0910f97c-44ad-30e9-93ff-21337a888d74 | -9.36764 | -50.66294 | 2024-10-19 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e383ff7a-f2e2-3f43-9e3d-948f7af3fabb | -9.37116 | -50.66346 | 2024-10-19 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f70cf5e-0196-3265-af56-cba3fdbf27b1 | -10.16192 | -54.89919 | 2024-10-19 04:51:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5005f853-4a66-3c0f-9a54-189e8293b623 | -10.15853 | -54.89864 | 2024-10-19 04:51:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fe7e68e-4768-376f-b999-022e5c64e34f | -10.15812 | -54.89838 | 2024-10-19 04:51:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7491f4c0-5a7c-3794-9290-be1e0619494d | -11.91808 | -55.27243 | 2024-10-19 04:51:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef9b01f-8c0a-32c1-bdcd-c4d817167436 | -11.28112 | -54.23989 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc1c8a85-7788-324d-b8d2-3c307acb026a | -11.27835 | -54.2358 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6e412394-7717-3ef9-a983-d0a54cbaf80d | -11.27779 | -54.23935 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad7a5c2d-3cfd-39eb-ab46-08c5f3b568e2 | -11.27502 | -54.23526 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 17806577-d33d-30b9-b027-f5eea96e2f36 | -12.27652 | -54.55177 | 2024-10-19 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c88a1cdc-9b01-38be-a485-f72c660af4aa | -11.28169 | -54.23635 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 117168d3-be3b-3657-b6cf-e7564b1c2681 | -11.27892 | -54.23226 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ccf888a-2ac4-38d0-b3df-7ac84a16ce7f | -11.27558 | -54.23173 | 2024-10-19 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README37.md)
