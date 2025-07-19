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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d8a4320-0618-358d-8db5-1a611be6eb38 | -3.1198 | -47.0075 | 2025-07-19 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 8d16cc6a-8ae4-3044-b620-0ad6bc014c3d | -10.7257 | -46.8006 | 2025-07-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 181aa47f-09dc-3ea0-8ec3-6ca43edf50e8 | -10.7257 | -46.8006 | 2025-07-19 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 595668e4-6c1e-33fd-a401-6ee0849cb452 | -3.1198 | -47.0075 | 2025-07-19 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 773c9b2a-e8f0-34ea-87a5-4d59862b4fa2 | -7.849 | -44.1941 | 2025-07-19 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d9ed5549-bc79-3303-b38c-2c92d8627987 | -2.8246 | -42.3818 | 2025-07-19 13:10:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 468a51f7-ad62-3a37-976f-875e9947b46b | -7.8302 | -44.196 | 2025-07-19 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 641ccc42-8874-3637-b3a0-9856330856d7 | -10.7261 | -46.7782 | 2025-07-19 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4e10c1ae-14e6-3cf2-9ec3-d8b6cda9c249 | -3.1197 | -47.0294 | 2025-07-19 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 53d00a10-688c-3f4b-94c1-72d0e6b83963 | -7.849 | -44.1941 | 2025-07-19 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 0bb1a41a-0270-38e6-9b25-92af076cd27e | -3.1198 | -47.0075 | 2025-07-19 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 516a707c-445a-37ce-8cbb-d827b5c2e03f | -11.4786 | -47.3306 | 2025-07-19 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e996d1e4-1f72-3ce8-bfe4-7b5462d221d2 | -7.849 | -44.1941 | 2025-07-19 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| d30b9b26-0621-3ee8-aa94-39a88b6d90eb | -3.1198 | -47.0075 | 2025-07-19 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 291d91b5-c703-32a4-92a5-fa6e72831bae | -8.0064 | -43.6672 | 2025-07-19 13:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9eec533a-edb6-3925-a4ec-ece43fc05a5d | -7.849 | -44.1941 | 2025-07-19 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 5d6505fa-c8e4-32e6-bf6c-9fd0c4d6d2eb | -11.4786 | -47.3306 | 2025-07-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 58a428bf-d780-3ed7-bcda-862a0b1133f7 | -11.4789 | -47.3082 | 2025-07-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 015d1708-f4c2-36fb-b0a3-ba80fb4988a6 | -7.849 | -44.1941 | 2025-07-19 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| bfc4547d-4acf-3f34-9e6c-49ec0e62053c | -11.4786 | -47.3306 | 2025-07-19 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9733e585-dec0-311f-8722-c052910c4817 | -8.0064 | -43.6672 | 2025-07-19 13:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d83691c6-0a47-3fa2-8785-19e4ac57b24f | -3.1198 | -47.0075 | 2025-07-19 13:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| b236188d-e59c-344d-be5d-0b5eca6dfea0 | -11.4786 | -47.3306 | 2025-07-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8a96028e-023e-3c2b-af39-5499624724cb | -3.1198 | -47.0075 | 2025-07-19 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 2c20ebf2-59d9-3705-b000-99831e2e246c | -6.8615 | -45.0882 | 2025-07-19 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 23989a3f-c244-31f3-827b-4aa405b86613 | -10.7257 | -46.8006 | 2025-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| cdd5ae03-1544-36c4-b85f-451dfb99d7fc | -6.7446 | -45.5282 | 2025-07-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fb15b8a0-adc8-3967-8122-7613c67d5064 | -10.7063 | -46.8254 | 2025-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 51318d4f-2314-3279-8c93-f0b91b335005 | -10.7067 | -46.803 | 2025-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| a70b7146-cd75-38f6-874c-606c49b0cc58 | -7.849 | -44.1941 | 2025-07-19 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 261167b2-6d76-309e-bf8c-ca86b57869b5 | -7.849 | -44.1941 | 2025-07-19 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| e0b399e4-8969-3abd-95af-bf762bfc4dfb | -11.4786 | -47.3306 | 2025-07-19 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| cf48abce-2d25-3aad-9d49-b5dd7f2dafc6 | -3.1198 | -47.0075 | 2025-07-19 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| e0ef5e07-ac0f-3146-89da-a10c6b41fb57 | -3.1197 | -47.0294 | 2025-07-19 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3ecba1ac-5282-3840-982e-8b26635f020a | -7.849 | -44.1941 | 2025-07-19 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| ce17f64a-80d9-363f-870c-31bec213c2b5 | -6.1799 | -45.8649 | 2025-07-19 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 45dcd8c9-923d-3dc7-8e0c-cd4cfa7f21aa | -10.8531 | -47.1648 | 2025-07-19 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2db8162a-dee1-3b15-b4f1-e9ad2a20c75e | -11.4789 | -47.3082 | 2025-07-19 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d88181f6-6bc8-3565-8e41-6b16d67067ec | -6.1612 | -45.8662 | 2025-07-19 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 16943f45-133a-362b-9367-e1aa6a9d38cc | -3.1198 | -47.0075 | 2025-07-19 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 584886c5-915a-3ecc-b4ee-21bb7627ac82 | -10.0308 | -46.3238 | 2025-07-19 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 18c451a2-bf08-35bf-999e-d3f1d4d90464 | -11.4786 | -47.3306 | 2025-07-19 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3bc5dd73-272e-398b-8145-e26fbc2f4f32 | -10.6835 | -49.6818 | 2025-07-19 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 97daa66f-8ac3-303c-a404-d5f6b25f67cd | -3.1197 | -47.0294 | 2025-07-19 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3b3708f9-e273-3687-adac-dbd6ed1b5a18 | -2.9733 | -42.5173 | 2025-07-19 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8014d5e2-ede6-3934-8ff5-cbff31d2a3e1 | -10.0308 | -46.3238 | 2025-07-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 83f0e33e-477e-317a-a179-27d14433ee9a | -10.8531 | -47.1648 | 2025-07-19 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 1ab733ac-d3cc-30a8-8c7c-b5f10eb6aa5a | -10.6838 | -49.6602 | 2025-07-19 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c3ada1b4-0712-341e-8a8d-009d9f5b7ae6 | -3.1198 | -47.0075 | 2025-07-19 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 9105f478-f34c-30c9-a680-cdc4f607d794 | -11.4598 | -47.3107 | 2025-07-19 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e8c7ffdf-3aa9-34ad-9ab2-cd4131380b46 | -11.4977 | -47.3281 | 2025-07-19 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8263b511-7697-3372-bcf5-bdc76c1fa6bd | -8.0064 | -43.6672 | 2025-07-19 14:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| dc8bf535-0c66-3ae2-995b-5576de1fea97 | -7.849 | -44.1941 | 2025-07-19 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3a38f30d-9d1c-396e-a4e8-d1bb5900f5a7 | -2.9374 | -42.2117 | 2025-07-19 14:30:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 0ddf72e0-c7ed-3b73-a8dd-8ab56ce2d206 | -10.0311 | -46.3012 | 2025-07-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bf00d66c-4db1-33e1-899b-4a4081bb4739 | -10.6835 | -49.6818 | 2025-07-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 691d445d-a66d-39ff-b489-9ea797589d6e | -10.8531 | -47.1648 | 2025-07-19 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 50e2f44d-cfb4-3f93-836f-416a25ea64de | -6.4895 | -44.8005 | 2025-07-19 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 32b1a5c6-ed4d-3c7d-bc92-260689fd2223 | -10.8722 | -47.1624 | 2025-07-19 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c8d97bef-a641-3a8a-b308-7b67ae55b315 | -7.849 | -44.1941 | 2025-07-19 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8d84b58d-3681-33fe-9e79-f3f3744dec3e | -10.6838 | -49.6602 | 2025-07-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0e6cc6aa-9456-37f3-b315-f309578a62e5 | -10.0308 | -46.3238 | 2025-07-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 2fbcb4b5-bb06-3dea-9690-a2f06815efb8 | -11.4598 | -47.3107 | 2025-07-19 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 24db4387-f37e-355e-a2ce-9b8a9e423c6e | -3.6798 | -43.0481 | 2025-07-19 14:40:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| e20bc1f5-b1f6-35b1-8b4a-0206f0b7aae1 | -11.4977 | -47.3281 | 2025-07-19 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |


