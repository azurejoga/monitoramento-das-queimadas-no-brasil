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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 885f10d0-57d1-3013-a272-65799d0ede7d | -17.3037 | -58.077 | 2025-10-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| bd5028a3-4cac-3c21-8c82-20d1ed111bc5 | -11.9519 | -46.4352 | 2025-10-08 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 8b7b0a52-9ca6-3542-a607-568e373faa48 | -10.456 | -48.3607 | 2025-10-08 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0e76add2-d425-3b5b-8c26-09365c435f0e | -15.6397 | -52.5474 | 2025-10-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bafd6fcc-8c61-3176-9248-295ad8092bf5 | -13.3211 | -47.1596 | 2025-10-08 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0801aeea-6cdc-3eb9-957f-2bd3c0bf8630 | -7.4666 | -43.0909 | 2025-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 137.2 |
| 0af0bb76-762e-30dc-b725-6602a0efb094 | -7.8896 | -45.5163 | 2025-10-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 1775d26e-583c-3fce-852e-3cfe561a60d2 | -13.0036 | -51.041 | 2025-10-08 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ecc78409-95a4-3306-a980-67cd1194ab9d | -14.7179 | -46.0867 | 2025-10-08 14:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 1b793010-c26e-3bae-9649-6c9c739593cd | -17.304 | -58.0566 | 2025-10-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 5cb73ea5-8810-3504-8bc1-1af08f2b05d1 | -13.3778 | -47.2185 | 2025-10-08 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 970ccc5b-7c89-3f2b-80d5-c12e2e4c4ffc | -12.3655 | -50.3049 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 094c2c31-1d7b-306e-96fb-38f4610946aa | -12.3911 | -51.1153 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3bf20eb3-1205-300a-99ca-eebb23df36d7 | -7.8307 | -44.1497 | 2025-10-08 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e3141919-9286-3696-b2be-819e6c902398 | -8.6106 | -45.102 | 2025-10-08 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 5c51038f-3499-3bd9-a281-f1cc2b285f54 | -14.7184 | -46.0636 | 2025-10-08 14:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 4d929007-4dcf-3aa3-ac1e-bc84c22f2461 | -15.3979 | -48.0164 | 2025-10-08 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e3e63708-9ca5-3629-8f46-390e8b15f68b | -10.748 | -50.4892 | 2025-10-08 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 167166d4-3412-3e5a-b554-a34470d6efdc | -4.0382 | -42.5129 | 2025-10-08 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| f764c2a3-4615-3bf4-9e00-911399513ce2 | -3.4366 | -43.1532 | 2025-10-08 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c12782d0-bbfb-3be8-8d0f-93c58d1931c7 | -13.3018 | -47.1626 | 2025-10-08 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 2fdb28a1-a0bb-3950-a055-8f422374dba9 | -11.785 | -45.0421 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5537500b-5f78-3e4c-9c12-da70fcafeba9 | -15.6202 | -52.5501 | 2025-10-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 48544e8e-ae7f-35a6-8652-70967458629b | -10.7472 | -46.6409 | 2025-10-08 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 946b6224-4994-306e-891d-95ae6bb62c7c | -10.4245 | -45.3907 | 2025-10-08 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 198.0 |
| d3035ccf-c330-31f9-935a-7bab2ee6ea78 | -12.1833 | -50.9905 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7b56bcfa-870d-35d6-9cfd-13b4f827f3f0 | -4.0569 | -42.5118 | 2025-10-08 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 206.8 |
| a3d7bbae-c78f-324d-8897-e6228360dca5 | -7.7919 | -44.246 | 2025-10-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 6b57cb23-eea3-3c96-8a94-a46434d0c650 | -7.7922 | -44.2229 | 2025-10-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 66916d29-22d1-3499-8242-370ca14d065b | -3.8946 | -41.5698 | 2025-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 28755988-a4b3-30b4-99b6-c08aed4fc46a | -7.7924 | -44.1998 | 2025-10-08 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.5 |
| d85f11f8-684a-35ce-a668-f46263439b63 | -8.1804 | -43.3445 | 2025-10-08 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.1 |
| 36bf2d84-bb7c-30a3-951e-9c0d748a201d | -8.1615 | -43.3465 | 2025-10-08 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 5cc94afb-2a92-33ed-90ec-45e1f7b31d6e | -11.1833 | -54.8787 | 2025-10-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 312.0 |
| febc64e1-fee5-3197-99da-83a87f0f40bc | -11.7846 | -45.0652 | 2025-10-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ce7d6c53-7c09-3ef8-b1cd-21fb2a6a3eea | -12.1649 | -50.9501 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 0244a8ca-975b-3842-aa87-4939b389f45e | -14.3884 | -46.0294 | 2025-10-08 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 162.2 |
| d43421b1-c18a-375d-89a0-e1729cfa7617 | -11.7573 | -51.5059 | 2025-10-08 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b85ca462-f8d8-3df2-a368-647286581db0 | -15.321 | -46.1622 | 2025-10-08 14:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bafacf65-7922-3b61-bf3f-028bfe022d6f | -13.2438 | -47.1714 | 2025-10-08 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3441955e-bf7c-3576-9e8d-7689d10462db | -7.4857 | -43.0655 | 2025-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| ff7e2d80-e49b-3483-9739-f879ab7c3b47 | -8.9383 | -44.6074 | 2025-10-08 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 92de0e75-8fa3-3108-80f7-79ca472825a8 | -18.0394 | -44.9438 | 2025-10-08 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 118.4 |
| aeff3421-c5c4-34b4-980e-2efed423f67c | -12.9816 | -46.7824 | 2025-10-08 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 161c87f0-4e05-3a31-b716-7d35fddd278d | -11.0265 | -50.8854 | 2025-10-08 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1e8fc871-eb1f-3372-9c6e-55000ebfbad9 | -12.1086 | -50.8926 | 2025-10-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 25768aaf-763a-3ddf-9c92-00edc6ae309c | -8.9005 | -46.0233 | 2025-10-08 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c0d97cc1-2e19-3588-9f7c-862711c64755 | -7.4857 | -43.0655 | 2025-10-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 92f0a9c4-e110-3f92-918e-759f870ed96b | -17.3037 | -58.077 | 2025-10-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| ca37e250-592c-395c-aaed-fd6c92c8b63e | -11.2213 | -54.855 | 2025-10-08 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ede7e800-1c04-3586-820d-b68cbb07568d | -10.9106 | -47.1353 | 2025-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 315a8927-945e-3eff-b06c-16e769f300f9 | -8.5398 | -46.2181 | 2025-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 67e196c7-5659-33dc-9f4f-aa716312d4c6 | -17.8611 | -57.6436 | 2025-10-08 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| b4b7a904-141d-34a6-8efa-4adb5942c755 | -12.2528 | -47.8505 | 2025-10-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| dee1307d-dab0-3743-bc43-c6fb770f2cc4 | -7.8307 | -44.1497 | 2025-10-08 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 1b0e182d-e82d-3de5-b855-fcc0d1733708 | -7.7919 | -44.246 | 2025-10-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 8ce38ef4-1783-31df-a2bf-cb614eea76be | -11.0104 | -50.6744 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 17a54b3d-09ee-3a06-9766-89eded3c4ec4 | -10.8573 | -53.7425 | 2025-10-08 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d741b17b-b448-3212-80fd-2b9816326de9 | -10.7291 | -50.4912 | 2025-10-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4469a963-dc40-3966-9a55-692ecfedf909 | -17.2837 | -58.0997 | 2025-10-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 9a34db4c-359d-35d8-a74c-3597e834f0e2 | -13.3513 | -47.6042 | 2025-10-08 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| dbe1f1af-1348-328c-85af-044f48d1b842 | -13.0036 | -51.041 | 2025-10-08 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 468b6621-9651-3a71-b80a-e0180e5d0a2a | -11.098 | -48.5489 | 2025-10-08 14:30:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 92f49cf4-c3ba-3ab6-8904-8dbf7323b2ab | -10.9296 | -47.1329 | 2025-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 82e15d63-8a89-3330-9a30-f8f2d3e1e3d3 | -4.1023 | -44.1379 | 2025-10-08 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d4634aa2-3544-3ef9-9698-a6541f89208a | -3.8948 | -41.5458 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 48da4dbf-93bb-39ac-9859-05ddd8d18d82 | -17.284 | -58.0793 | 2025-10-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 07778b61-2138-3f95-a1f6-1faf05bc0007 | -3.8048 | -43.9923 | 2025-10-08 14:30:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ef171474-0607-37d1-ba03-67499b20874d | -8.8794 | -47.6722 | 2025-10-08 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| f5bdb638-242e-385a-9cef-4410d6d4f776 | -14.7184 | -46.0636 | 2025-10-08 14:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 38e825e9-4943-3fd8-a123-e2156457f320 | -4.5033 | -42.862 | 2025-10-08 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f8cd7ebd-c15e-319f-b98d-f8d853b5043f | -3.8573 | -41.5479 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 186.9 |
| 2d41899d-a9aa-37cd-9c56-8fa1e3ecb8de | -12.3846 | -50.3026 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4820ad7c-a08a-3dd4-946a-876cee392b82 | -12.7157 | -47.6748 | 2025-10-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4cd5e773-4b87-3ec4-9d71-2208d9680a03 | -10.748 | -50.4892 | 2025-10-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2a6be26c-731e-3ef7-97df-4993e4e47571 | -3.4366 | -43.1532 | 2025-10-08 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 215f12d8-2d0b-3ec6-a1d0-6374b8a50d0a | -12.6478 | -50.571 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| f0af6266-f325-39dc-84bd-8f9f53342c8b | -5.381 | -40.9871 | 2025-10-08 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 178.3 |
| b940e85b-c743-3665-869b-51ec9cc3c93b | -8.88 | -47.6282 | 2025-10-08 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 54ff4051-0430-3b9b-b259-371b7d708c68 | -12.0118 | -45.2161 | 2025-10-08 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| cf27811f-3a4b-3855-b993-a3d0a4fe5d58 | -12.385 | -50.281 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a2544bc2-a56a-3197-8e58-4b3e6e1fd331 | -13.2847 | -48.0827 | 2025-10-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 30dea0a3-e3aa-3ff9-a6c7-74aa397f81da | -14.8645 | -51.4158 | 2025-10-08 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2783d790-41b3-3e22-8628-41c1db5e9f62 | -10.8732 | -47.0953 | 2025-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7c70cfaa-2f3d-3d99-b132-a216ecbb88f9 | -12.3911 | -51.1153 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5279cc50-9caf-3125-a0b0-33979250c63a | -17.304 | -58.0566 | 2025-10-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| a61121e6-53bf-3389-849b-495fb3bbad75 | -12.1833 | -50.9905 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e149d659-fa3b-3d3f-8688-51d2027d9a88 | -10.8919 | -47.1153 | 2025-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| df5a459b-466b-3263-abbb-d0eff5f626ac | -5.3622 | -40.9886 | 2025-10-08 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 166.3 |
| ebc202c7-ea38-398d-82cc-77287ea82d36 | -12.9816 | -46.7824 | 2025-10-08 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1cc8d897-1d25-3bb1-bd92-3005e7f9a1c2 | -7.9085 | -45.5145 | 2025-10-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8f7458de-4cab-389e-906c-842223f9bc4d | -11.785 | -45.0421 | 2025-10-08 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9179f80a-7d8d-3945-950c-b2df862b0ab3 | -14.7179 | -46.0867 | 2025-10-08 14:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 9120e9e2-161a-3f51-8204-bb60f8887dc6 | -12.4044 | -50.2571 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0e8ad831-141c-36da-9e17-06860a2c695f | -10.8762 | -53.7408 | 2025-10-08 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d1b04fab-bb51-3463-8fed-f380d6fe5395 | -10.7468 | -46.6634 | 2025-10-08 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b708757c-ff87-39df-acf9-483b75cd4488 | -11.4534 | -50.198 | 2025-10-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 58544cbe-9a06-386e-a54f-78f8e2d57db0 | -14.8451 | -51.4185 | 2025-10-08 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 42e680f7-eb9d-3b28-a01f-1688df6f33dd | -7.8119 | -44.1516 | 2025-10-08 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b3f5bc0a-2724-3f7a-b9fa-8fb5a886eec1 | -18.0193 | -44.9485 | 2025-10-08 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |


[Clique aqui para ver as próximas entradas](README111.md)
