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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd09053-e561-3b78-aa8f-f88b8e921f8b | -6.8448 | -55.5411 | 2026-09-21 11:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c23c2362-9086-3abb-94c0-d1cae5eb07de | -7.4092 | -44.7885 | 2026-09-21 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| e21e8163-fc87-3379-bda9-f52e51638bc4 | -6.8263 | -55.5421 | 2026-09-21 11:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| fc5eb3b2-0a76-30a3-a67f-483830a44e45 | -12.9091 | -50.9672 | 2026-09-21 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2ff2cf88-79f8-35b3-9113-bcbaef08b7db | -12.8246 | -54.0442 | 2026-09-21 11:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1454a175-54ab-3575-b6c4-9f13860ca846 | -11.8495 | -46.833 | 2026-09-21 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| deec8985-685a-37e2-9915-4c692b8ab674 | -10.3917 | -48.8915 | 2026-09-21 11:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c4a82eaf-c4c2-396d-929e-71ee2c03ecba | -12.8437 | -54.0422 | 2026-09-21 11:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e7374cae-81ea-3c48-85aa-1aa1ec789ff9 | -7.428 | -44.7867 | 2026-09-21 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| b8991d2c-32b7-311b-a030-a656061e8ff9 | -10.8011 | -50.7604 | 2026-09-21 11:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0c01e036-0952-3a48-ad5a-64045e8b254a | -10.8197 | -50.7797 | 2026-09-21 11:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 288fb95a-7385-3a9c-a8b6-db4febe3c145 | -7.5661 | -42.656 | 2026-09-21 11:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 36dd2b67-7c94-3923-acb6-6d1e7d92c435 | -7.3291 | -55.1955 | 2026-09-21 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e2a48c6f-fef5-3762-8265-d185b33d2f49 | -7.4092 | -44.7885 | 2026-09-21 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 91780918-70bd-3495-8562-340a55721c55 | -8.7726 | -44.28 | 2026-09-21 11:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 01fba1b4-b446-3c67-8763-4b018ae5f172 | -7.428 | -44.7867 | 2026-09-21 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b843100f-a308-3fdf-8726-8993c3ffc13c | -12.8437 | -54.0422 | 2026-09-21 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 225.0 |
| 7ec45c54-218a-34c9-b21a-c62eb8668573 | -11.8682 | -46.8529 | 2026-09-21 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b0b803cd-43fd-35f9-be9f-aea7df09300b | -10.4297 | -50.2663 | 2026-09-21 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9c7ba2de-f7c3-3fbd-af6b-f96dba9ec169 | -6.8263 | -55.5421 | 2026-09-21 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6b755e05-45bf-3321-8541-1b6af8bd09ed | -10.4672 | -50.2838 | 2026-09-21 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 976d4f76-eee4-3e42-835c-b46d6fa11095 | -10.3924 | -50.2275 | 2026-09-21 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a3657b78-5049-3422-b023-edd81a299e91 | -12.8246 | -54.0442 | 2026-09-21 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 181.8 |
| a4f64b24-afa5-3769-a1c4-4672a1352563 | -7.5661 | -42.656 | 2026-09-21 11:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 4d46714f-bbd2-3688-a001-a2b8839c575c | -12.8434 | -54.0629 | 2026-09-21 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 60c8613f-5d58-3226-af17-2352f8000ced | -11.8495 | -46.833 | 2026-09-21 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 4b589435-4759-37df-ab20-b5ca5ecf679b | -10.4486 | -50.2644 | 2026-09-21 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 72d96996-c27b-340e-b281-d40acbc17dc2 | -6.8448 | -55.5411 | 2026-09-21 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 820b1231-685f-3c68-b250-da46411c0853 | -11.8491 | -46.8556 | 2026-09-21 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fa76eced-8385-3e7c-973e-3278892b5426 | -9.8689 | -48.4252 | 2026-09-21 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0202bb0f-2d83-34b0-900c-6e402f885476 | -12.8437 | -54.0422 | 2026-09-21 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 77b73938-b465-3d39-b021-f307dda50af6 | -9.8689 | -48.4252 | 2026-09-21 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ce21a50a-fee1-3971-9941-134b24e4ea1d | -11.0997 | -51.0687 | 2026-09-21 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a2c31dd6-5b2f-35de-be2e-e5f3d674399f | -7.428 | -44.7867 | 2026-09-21 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 944de77f-9e29-38e8-bd41-33a3cadc546b | -7.3291 | -55.1955 | 2026-09-21 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6e923843-2981-3d46-b7bc-2786d6553a8f | -10.8011 | -50.7604 | 2026-09-21 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 93a0493c-f8fa-3251-a594-8cd8f1495962 | -10.8197 | -50.7797 | 2026-09-21 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| e7e79cac-30c5-3783-bb21-4cefe009ce37 | -12.8708 | -50.9719 | 2026-09-21 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 18b8d07f-b0f7-376a-96a1-0e65fcc0cc95 | -6.8263 | -55.5421 | 2026-09-21 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 4e8d5fe3-adc2-3e86-b307-38508f06e2ad | -12.8434 | -54.0629 | 2026-09-21 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 20bad379-4cb0-3c21-96bd-2cfb1aa1638b | -10.8014 | -50.7391 | 2026-09-21 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9fdf1331-7947-3a2c-9205-234599da4f78 | -11.8495 | -46.833 | 2026-09-21 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e0e29748-6613-3b18-879f-2bfe310a4b26 | -8.4123 | -45.8712 | 2026-09-21 11:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28970ce4-ec06-3403-a801-af62f7bae43a | -9.831 | -48.4292 | 2026-09-21 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 500e0882-1918-3bb2-b24c-1fc2ea381dbd | -12.9091 | -50.9672 | 2026-09-21 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7d77c81e-9a09-399c-9079-1dd75dcabaf8 | -10.3924 | -50.2275 | 2026-09-21 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 9543b701-4110-3d9e-81cb-e89afdefe008 | -10.3917 | -48.8915 | 2026-09-21 11:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 63e811ba-4e40-31c3-9283-b4cafea8f1bf | -9.8307 | -48.451 | 2026-09-21 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| d6ba6ae9-71ac-33ac-a09f-aaa342526754 | -8.7911 | -48.7502 | 2026-09-21 11:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d172f0e0-f3f4-37b2-96b8-e491db2d05c5 | -9.4567 | -45.4178 | 2026-09-21 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 422f90eb-99f2-3237-ad79-609de8d1b38c | -9.8686 | -48.447 | 2026-09-21 11:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1b4ae3ae-0b4e-3426-91b1-959309b8ff1a | -6.8448 | -55.5411 | 2026-09-21 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 66390455-41d0-3447-a9e0-e9c011cfaddd | -12.8899 | -50.9695 | 2026-09-21 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e6f2460e-38c0-3233-be6b-3fd52bd03b8b | -8.7726 | -44.28 | 2026-09-21 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fdfd2544-8226-3311-9c40-e4dfba9a4174 | -7.4092 | -44.7885 | 2026-09-21 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| d799f0f9-e56b-38dc-b056-0bb7ee9d716e | -11.8682 | -46.8529 | 2026-09-21 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| a6c7a244-8f9b-30d6-be60-135edda8efbc | -10.4113 | -50.2255 | 2026-09-21 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d7b9a820-bacd-3817-9769-6bd010ee38eb | -7.5661 | -42.656 | 2026-09-21 11:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 2d9b99dd-fdaf-3eee-874c-8526167dff8e | -12.8246 | -54.0442 | 2026-09-21 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 838d78a0-5672-39ca-9300-7dcf85832a7e | -11.8491 | -46.8556 | 2026-09-21 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 578d686d-3356-3bdb-b90e-3b2a4f8351c5 | -12.8244 | -54.0649 | 2026-09-21 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7a7806ac-82b4-3df5-9c51-e3da7cc193ee | -10.3917 | -48.8915 | 2026-09-21 12:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c11f8052-1285-36a2-b648-28881b0a22dc | -11.8495 | -46.833 | 2026-09-21 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 60330248-f130-3069-b83f-f68bce5430fe | -11.041 | -54.1567 | 2026-09-21 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| bf3e1696-63c5-3f54-a855-4b446bab4a43 | -12.8244 | -54.0649 | 2026-09-21 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b3ada571-a1bd-3692-b64f-9ef68d8338f5 | -12.8246 | -54.0442 | 2026-09-21 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 179.0 |
| e20e3b0c-bb45-3285-998d-8f48e6126e96 | -12.9091 | -50.9672 | 2026-09-21 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 21f27557-6642-351f-a94a-14435b41489d | -10.3924 | -50.2275 | 2026-09-21 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 20b6d7d2-8d1a-3d70-b3e8-505ae618a869 | -11.8682 | -46.8529 | 2026-09-21 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 0ea2a312-3826-3e09-86f3-e4f3ab24a418 | -11.0997 | -51.0687 | 2026-09-21 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 467d0eed-afba-34d3-b403-8e63516f8e59 | -12.9283 | -50.9648 | 2026-09-21 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1a63084a-1497-3f88-ad21-c6beaa7df879 | -7.428 | -44.7867 | 2026-09-21 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a2dd3d2c-d79b-3e53-a022-46c7b828b7c9 | -9.8686 | -48.447 | 2026-09-21 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1717d532-c30c-3f7f-8ed4-5c986a602110 | -6.8448 | -55.5411 | 2026-09-21 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| ad8e06a6-bbb1-34b1-820d-e06b3d38e220 | -10.8011 | -50.7604 | 2026-09-21 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 56b2f3f7-248c-353e-b8c3-50b3dc45acbd | -7.5661 | -42.656 | 2026-09-21 12:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 4df58ac1-8816-3853-be1e-28a1045eb9c7 | -11.1 | -51.0475 | 2026-09-21 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 92cd38c1-aa2b-3a15-a0e4-fa78d72548a2 | -12.8437 | -54.0422 | 2026-09-21 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 426.4 |
| 8e5e3fd0-dbf5-385b-9b3c-ed330efd8f08 | -7.4092 | -44.7885 | 2026-09-21 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 35fdd4e7-8cd8-3b8f-958f-ff5b05010f2b | -9.8689 | -48.4252 | 2026-09-21 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3388ac80-6bd4-3b21-92b5-8b4421a67eff | -7.3291 | -55.1955 | 2026-09-21 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a8ee5721-ae86-3335-a23a-6e8f6d94e8af | -6.8263 | -55.5421 | 2026-09-21 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cbe55a00-a927-3e53-86e9-3a4f5cff3c97 | -11.0412 | -54.1362 | 2026-09-21 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 45c1b384-829e-3c85-9a78-cd4e6303f5c3 | -12.8899 | -50.9695 | 2026-09-21 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 83069201-1d04-37b9-88ed-e9fbd195f15b | -10.4113 | -50.2255 | 2026-09-21 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5767dc07-ad89-396b-a030-2adb5ad5bfce | -11.8491 | -46.8556 | 2026-09-21 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 167c8cd0-7f20-30b3-a521-176cce17e971 | -12.4204 | -47.0228 | 2026-09-21 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9f5edce2-ae59-384e-b9c9-2bedffcd79e8 | -8.7726 | -44.28 | 2026-09-21 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 99ba655d-d405-3d1a-82e5-36e818a90ce3 | -9.8307 | -48.451 | 2026-09-21 12:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d61d8337-9bd5-3102-9b1a-5618466c0bf8 | -12.8434 | -54.0629 | 2026-09-21 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| e62253b2-077b-3632-8adf-301fa12c5bc6 | -10.8197 | -50.7797 | 2026-09-21 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8a2e84b3-839a-3a58-9b01-25587407469b | -7.3289 | -55.2155 | 2026-09-21 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f2a65419-0c31-34a3-a0e1-b4a379526b41 | -11.8491 | -46.8556 | 2026-09-21 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e66c5642-73ce-3426-9dc2-75283dc89bbf | -9.8692 | -48.4033 | 2026-09-21 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 27e528a5-9792-3d64-bb1f-6f12f00a35d3 | -12.4204 | -47.0228 | 2026-09-21 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fc549741-f012-3fbd-875b-50d59f6c75cb | -10.3924 | -50.2275 | 2026-09-21 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 75852bde-76ba-3a18-9dc8-b893c8683289 | -9.8689 | -48.4252 | 2026-09-21 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d8da2daa-c727-338b-bfe4-d6fdf8e24523 | -6.8264 | -55.5222 | 2026-09-21 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fa3fc0e9-9c1d-3551-82b5-1990c920f982 | -11.8682 | -46.8529 | 2026-09-21 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 9ec6e261-a5e4-37dd-b0ff-1642de57b69e | -16.0104 | -52.5163 | 2026-09-21 12:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README113.md)
