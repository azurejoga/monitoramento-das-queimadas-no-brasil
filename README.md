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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd15f2b6-3f56-3415-9239-b0c30913c519 | -9.1222 | -46.3816 | 2026-08-15 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e7795ede-a09e-365f-b67b-053069fc5984 | -6.6194 | -59.0609 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 32fdb567-fed2-3936-8f17-96526bba4aea | -6.7123 | -58.9412 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d35deea7-2375-351e-a40e-c3da1b9c6401 | -6.7872 | -55.8425 | 2026-08-15 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c009e4b8-4a9c-307f-9a1b-dbac8bff9e6a | -6.9331 | -43.6566 | 2026-08-15 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f42bbf24-a5b2-333b-9003-358dd07213be | -1.5805 | -47.7462 | 2026-08-15 00:00:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 3ca8a140-1f93-36b4-9e0d-9b58ed1f9272 | -6.6193 | -59.0802 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a32881ca-30ca-3e09-8fbf-cc8227f9c67c | -11.4004 | -46.2852 | 2026-08-15 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 20c0c21c-6f95-381c-9da0-50e6c96ab6ef | -6.6197 | -59.003 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| fddc4f63-c945-31a0-9ff7-2addd9ddd81a | -6.95 | -59.2984 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8b5dfdab-e058-3c3f-9e78-b7071db20cdf | -14.4544 | -45.6716 | 2026-08-15 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 255dce25-2d1e-3f79-b6b1-59862d794d71 | -11.4 | -46.3079 | 2026-08-15 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 039fbe9e-531f-3d7d-be45-60ece1d6a76c | -9.103 | -46.4061 | 2026-08-15 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 088aaaa5-7a40-320c-ac2f-3add446f40db | -8.9601 | -60.5165 | 2026-08-15 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1337f05b-54e3-387d-9383-020ea37d5a76 | -6.9336 | -43.6101 | 2026-08-15 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 44368e5c-71c2-3946-bc4f-4cde2e93ee0d | -9.1219 | -46.404 | 2026-08-15 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 4eaeb52b-b5d0-30f7-9e63-7bace6d39ed8 | -6.6195 | -59.0416 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d571fe0a-76f4-3fc3-ad72-e5021f94f4ff | -6.9145 | -43.6351 | 2026-08-15 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 150.5 |
| acfccbc2-f1b8-3967-b307-7f4f6b1612ff | -9.1408 | -46.402 | 2026-08-15 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 27efb98e-bcbf-35ae-915d-11702aa2f8b8 | -6.9334 | -43.6333 | 2026-08-15 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 0871739b-cb75-32a0-9690-208b98ac0712 | -4.113 | -42.5087 | 2026-08-15 00:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 67b8e26b-ad74-3a75-a934-79d3d76986d3 | -6.1222 | -44.0271 | 2026-08-15 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 75435c56-f9c5-3f63-8d3e-9377e4c5e5f6 | -6.9685 | -59.2976 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 36f3731c-9e45-3dcd-b825-a83936a92645 | -6.9502 | -59.2791 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 88f1fa71-38b9-383c-ac18-f35c68bc527d | -6.8388 | -56.4146 | 2026-08-15 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c007fd81-f078-35cd-a9eb-76820a40b8a4 | -6.8387 | -56.4344 | 2026-08-15 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b8659873-a135-385a-81ff-4449a083cbbf | -6.6013 | -59.0037 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 40b45d0d-3ab4-358c-8058-b9e60e1442b7 | -11.3809 | -46.3105 | 2026-08-15 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d0193266-f193-34bb-aa59-9aeb5dd1acf7 | -6.9686 | -59.2783 | 2026-08-15 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 87d7d8a4-c7e7-3cd9-8c98-eca5835bf95f | -9.1408 | -46.402 | 2026-08-15 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 7cad4f20-9ceb-3a79-8dfd-44b6f74ae876 | -7.4582 | -55.2883 | 2026-08-15 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e79125ab-2dfb-3466-bb6c-d6edecee54af | -14.4544 | -45.6716 | 2026-08-15 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| ba867701-7646-35bd-9281-77de70d5a15c | -6.1222 | -44.0271 | 2026-08-15 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c93dee66-9328-362f-96a3-db10375faecc | -6.6195 | -59.0416 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f90dcb8f-09f0-3c78-86bd-5ee14e997f5b | -6.9685 | -59.2976 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2d525ad0-5edb-3198-816a-e5f9198acbaa | -6.9686 | -59.2783 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| efc839ff-4b1d-30f3-b485-2a924e8fe3ca | -6.8387 | -56.4344 | 2026-08-15 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 443aa328-d3e9-3c8c-90d6-2f749ed4b077 | -6.95 | -59.2984 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bff54bfe-1cf5-3442-bd24-561de00fec6e | -11.4 | -46.3079 | 2026-08-15 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ec21fcff-ad59-34ba-a096-25fb5758b5ba | -9.103 | -46.4061 | 2026-08-15 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ab881f0d-1d8c-32ba-8c75-dce1a0e30425 | -7.458 | -55.3083 | 2026-08-15 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 33a5aead-0bc9-3963-9b63-338a95aed092 | -9.1219 | -46.404 | 2026-08-15 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| f5c691e7-b57f-380d-82a8-e8fba5c2934f | -6.6378 | -59.0602 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a254ca34-5204-3936-b56b-411d292f886d | -11.3809 | -46.3105 | 2026-08-15 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b0232126-5c84-3e2c-864a-a96d7a1502b9 | -6.7872 | -55.8425 | 2026-08-15 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6c802c66-97e0-3d46-bbcd-038ccaa9504b | -6.6194 | -59.0609 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 8ae050f2-7405-394d-861f-55f6b5c16a86 | -6.9334 | -43.6333 | 2026-08-15 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 1a12ca1e-4aa7-3aca-b2d7-0e51aed5f12c | -6.9145 | -43.6351 | 2026-08-15 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| a1514c97-5948-3ad7-8c69-b45b0c1f4fb1 | -1.5805 | -47.7462 | 2026-08-15 00:10:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 8bb90c29-b012-3c76-ad4d-27770abc2292 | -6.8388 | -56.4146 | 2026-08-15 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5be38fc1-6e07-34c1-8fbe-5496b7a075b7 | -8.9601 | -60.5165 | 2026-08-15 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 39dd67b3-914e-3db5-a57a-5a5215a89665 | -6.6013 | -59.0037 | 2026-08-15 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6bfa4f0b-3494-3521-8c37-0b5fc42aa603 | -9.1222 | -46.3816 | 2026-08-15 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8cc7ab0c-debd-3628-9481-7e33271ba958 | -7.458 | -55.3083 | 2026-08-15 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ba153c72-44a0-30b8-a925-579a068673ca | -11.3809 | -46.3105 | 2026-08-15 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c330a9e8-091c-3e6c-a76d-05d6a1f815e5 | -9.1408 | -46.402 | 2026-08-15 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| de2535aa-0102-3f5d-b9ff-677a0ca3dbfa | -9.1222 | -46.3816 | 2026-08-15 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 61df1db9-81ce-3ab6-9533-6bd776861a6a | -6.9334 | -43.6333 | 2026-08-15 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 7bfde06c-b957-3d2f-a744-da5c73e3c9fd | -6.6194 | -59.0609 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ad13b26c-958a-34fa-b658-b050c0029cc1 | -3.9785 | -49.4563 | 2026-08-15 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d210ddec-28d2-33da-b239-afbe2ef6a4aa | -6.95 | -59.2984 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9e2e9052-432d-334b-aa5a-62914020658b | -6.6378 | -59.0602 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f2782ff2-76db-3231-ae80-c3e72b186328 | -9.103 | -46.4061 | 2026-08-15 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ad9f22b0-1ede-32f8-8c55-02abf9f0f0bd | -9.1219 | -46.404 | 2026-08-15 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 173e3f2c-1b57-3fbf-870b-fc1cb98c8132 | -6.6195 | -59.0416 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 492abc1c-2bf7-3365-92c9-e8908d178b10 | -14.4302 | -51.9243 | 2026-08-15 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 94c08d40-b060-38aa-bfe9-a098e4c52372 | -8.9601 | -60.5165 | 2026-08-15 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 70b4aea8-9947-3896-a146-2dc07e10701c | -14.4495 | -51.9217 | 2026-08-15 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3b40fd65-6b7e-3222-8282-dfcf11ad01d2 | -6.1222 | -44.0271 | 2026-08-15 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 97f2b883-5f55-3394-8d14-e99150e0e9f5 | -6.9145 | -43.6351 | 2026-08-15 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| be8aafea-81d1-3a65-a86b-e42e907804ea | -11.4 | -46.3079 | 2026-08-15 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 104a6e73-66e1-37c6-bbfd-b631bebf378b | -14.4499 | -51.9004 | 2026-08-15 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 63703efc-5dc1-3fd8-b340-45e754a44e83 | -6.9685 | -59.2976 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 156de58f-52b7-3cdf-a786-6d9293e73c53 | -6.8387 | -56.4344 | 2026-08-15 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2d4b08d3-930b-3a2a-b1a9-1b560092f735 | -6.6197 | -59.003 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b7a0bbe8-33b9-3e08-a550-a6960c2e8767 | -6.9686 | -59.2783 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ce0bb0be-e14f-3a47-8677-d2f387947304 | -6.6013 | -59.0037 | 2026-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| c8aabf1f-22d2-3d51-afd8-ef2ca96e4bd1 | -6.9331 | -43.6566 | 2026-08-15 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| df720847-3eeb-3693-9a34-386a20ef8bd9 | -8.9041 | -60.5577 | 2026-08-15 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 776f6ee4-a8fc-3065-9e7e-1fd36c4ade38 | -6.1222 | -44.0271 | 2026-08-15 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 96f781c6-12ed-33f7-b383-c3f0f74187e6 | -6.6197 | -59.003 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0a5360c8-9682-3bd0-adb2-36b01cdc1076 | -6.9685 | -59.2976 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4d64cd97-e3f4-39c4-8217-9520d57a5bf5 | -6.9334 | -43.6333 | 2026-08-15 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 2683fc0b-b1ff-3c12-af7d-9b51ddcd0e16 | -14.4499 | -51.9004 | 2026-08-15 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 34f67617-0dbe-3763-847b-5598b542ba08 | -14.4306 | -51.9029 | 2026-08-15 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f5dcfe46-e8cd-3411-ae58-d35915154703 | -6.95 | -59.2984 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| dfbcf0dd-927e-362f-a977-4329dd325f34 | -14.4495 | -51.9217 | 2026-08-15 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f87d0e86-4da9-341a-906e-f188e55ed546 | -9.1222 | -46.3816 | 2026-08-15 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8c45712b-8b90-3e5a-a4f8-77338049333b | -8.9041 | -60.5577 | 2026-08-15 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 04a72128-eda6-34b6-8c34-36d3b83e423d | -14.4302 | -51.9243 | 2026-08-15 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a5906604-3515-37fa-86c4-dc310be95335 | -6.6194 | -59.0609 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 134c5b1f-af09-31be-ab97-ab7d21ad2f58 | -6.9686 | -59.2783 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a62725c1-9c3a-3108-a482-e22592d6a964 | -14.4492 | -51.9431 | 2026-08-15 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5664cde6-5a82-3449-bffe-d8f4f942a11f | -6.9336 | -43.6101 | 2026-08-15 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c4ba94e5-84be-3c1c-8cbe-09cea7f13edc | -3.96 | -49.457 | 2026-08-15 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 43fb8a1d-c7aa-3bd6-a193-1e8c7ee77c1c | -9.1219 | -46.404 | 2026-08-15 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 72b03ad3-5da9-36c1-a9c0-3c8777f98238 | -6.9145 | -43.6351 | 2026-08-15 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 085d76af-ce12-31bc-bff5-f88c3c6cb384 | -9.103 | -46.4061 | 2026-08-15 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 55060a53-b62a-39e6-9b43-79adb654917d | -6.6013 | -59.0037 | 2026-08-15 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 522e7444-62ea-384b-8da7-e8b93671208c | -8.9601 | -60.5165 | 2026-08-15 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |


[Clique aqui para ver as próximas entradas](README2.md)
