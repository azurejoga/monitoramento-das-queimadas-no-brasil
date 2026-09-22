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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2e3a4c-356a-347a-993b-fca9a31d0fe5 | -6.6148 | -59.908 | 2026-09-22 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7dae34de-a764-34b7-9996-1f9983ff4760 | -6.6332 | -59.9073 | 2026-09-22 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 73b7126d-9a89-359e-bd1c-29d404042ef6 | -12.8715 | -50.9291 | 2026-09-22 07:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 3a85f23d-f28d-306c-a581-994a4dc9cc18 | -10.6094 | -53.9902 | 2026-09-22 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a79af487-c5f9-39b0-b350-de6e1c4697c6 | -12.8718 | -50.9076 | 2026-09-22 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 186.7 |
| f3143613-d4e4-3672-b4e8-b27b05c1d6a7 | -12.8906 | -50.9267 | 2026-09-22 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 4cc5689b-ffe1-3994-b10c-757475a627f3 | -12.3025 | -50.6774 | 2026-09-22 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 871adf28-1fea-34f6-8729-2faaaf9b51a4 | -12.8715 | -50.9291 | 2026-09-22 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 7b8c8ee9-5bc8-322e-828c-be9cc5b042d8 | -6.6146 | -59.9272 | 2026-09-22 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 5338b09e-dccd-3434-8dfe-47e5729cb914 | -6.6515 | -59.9258 | 2026-09-22 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 60da82da-412d-351b-93cd-23b665e56022 | -6.6148 | -59.908 | 2026-09-22 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 32f70e47-6fa1-3b7f-9052-a7cbca3542b2 | -12.3021 | -50.6988 | 2026-09-22 08:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 5c72b8e5-e5fa-33a4-a889-6dc230444bb0 | -12.891 | -50.9052 | 2026-09-22 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 0b6daee7-d613-3706-8082-6012d3ab5a98 | -8.6135 | -62.5171 | 2026-09-22 08:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a4366f70-0f9d-3bf0-a730-a712bb454ca3 | -6.6331 | -59.9265 | 2026-09-22 08:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c616e280-7eb5-3e86-a8a5-1474e3aa081b | -12.891 | -50.9052 | 2026-09-22 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 12f7ba8f-caff-3061-9111-d7206e297b2d | -6.6331 | -59.9265 | 2026-09-22 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a2dc8d7f-ad97-3a25-aeb8-6f5b9e4fea59 | -8.6507 | -62.4966 | 2026-09-22 08:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3cfce342-2603-33ef-83c6-78f7d730e2d3 | -6.6515 | -59.9258 | 2026-09-22 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5a31f7b2-a1b2-3e64-804e-a3280640a797 | -12.8715 | -50.9291 | 2026-09-22 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 69189092-5330-306f-af87-22f9946490c6 | -6.6146 | -59.9272 | 2026-09-22 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 11fa7edb-b36d-33ca-9586-35c5328f6812 | -6.6332 | -59.9073 | 2026-09-22 08:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 32953559-a547-36d0-942a-abd7052be267 | -12.8906 | -50.9267 | 2026-09-22 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 228.2 |
| e86b894f-3d7b-36dd-8603-afd85918dc97 | -12.8718 | -50.9076 | 2026-09-22 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 192.8 |
| d8ed3a47-e5ac-341a-8e64-4a29456e9f16 | -12.3021 | -50.6988 | 2026-09-22 08:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| fa1700c4-788e-317e-a1d6-3911040328bc | -12.3021 | -50.6988 | 2026-09-22 08:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c4a5ad4f-b2f2-3001-8561-bd80a5c79c6e | -12.891 | -50.9052 | 2026-09-22 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 8436f9dd-4679-3e21-a48f-8d0cbe8278fe | -12.8718 | -50.9076 | 2026-09-22 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 04e51fed-0cc2-3335-ac61-0e7dad0ad388 | -12.8906 | -50.9267 | 2026-09-22 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4a6cffb4-72d8-33a3-ae37-8341f3983e7c | -12.8715 | -50.9291 | 2026-09-22 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9aea4263-c3e5-3277-ba23-5f24dcfb87e0 | -6.6148 | -59.908 | 2026-09-22 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8eb7b003-6645-3d55-af70-7e6bf9702898 | -6.6146 | -59.9272 | 2026-09-22 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8423b2e3-73af-31e6-9175-f4679185c3ca | -6.6332 | -59.9073 | 2026-09-22 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 753c8d3c-5085-3e8a-9c94-25fedfb3f018 | -6.6515 | -59.9258 | 2026-09-22 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 875875a9-cc77-3fc7-b029-bd898b4c7fd6 | -12.8913 | -50.8838 | 2026-09-22 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ed07e4b7-19fb-305d-b3ac-24a3012945ee | -6.6331 | -59.9265 | 2026-09-22 08:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 13f16d1f-5a6d-34ce-8402-30695d931bba | -8.6135 | -62.5171 | 2026-09-22 08:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b6d761de-0f9e-3298-8902-6a442a791ac7 | -8.6322 | -62.4974 | 2026-09-22 08:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 14e3c405-bfcb-3aeb-b7d6-77aa617309d4 | -10.6094 | -53.9902 | 2026-09-22 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 502a63d8-ffa1-385e-b30b-341736b2760c | -12.3021 | -50.6988 | 2026-09-22 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 49785a94-188d-35b4-b302-31cd5347824c | -6.6332 | -59.9073 | 2026-09-22 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8d1ff69f-c04d-348b-be99-def694de18b1 | -12.8715 | -50.9291 | 2026-09-22 08:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0d0ca21a-1b28-3bf2-83b2-0dc757ae7193 | -12.891 | -50.9052 | 2026-09-22 08:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cedcf5cf-73e2-3788-8558-0af12aa88dec | -12.8718 | -50.9076 | 2026-09-22 08:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| a716a9b4-8f40-3c45-af8a-52fb18efb8c8 | -6.6148 | -59.908 | 2026-09-22 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3d56d57a-80cc-3e52-9256-0be287abc8e5 | -6.6515 | -59.9258 | 2026-09-22 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 11d40eba-fe31-3235-a62b-0b97ee4772c9 | -6.6331 | -59.9265 | 2026-09-22 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 62d6048a-c23c-3490-9add-bd1d899ddaf9 | -6.6146 | -59.9272 | 2026-09-22 08:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a97bb15b-153a-3569-ae69-cbf50e887cf5 | -12.283 | -50.7011 | 2026-09-22 08:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 115e64bc-c0c4-3246-beba-0d9d42a08d5f | -6.6515 | -59.9258 | 2026-09-22 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| d2a05310-2a05-38cd-8be1-9c3cdaaa46e4 | -6.6146 | -59.9272 | 2026-09-22 08:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| fc76cb3a-0323-3723-9d36-60d0f4e354a8 | -6.6331 | -59.9265 | 2026-09-22 08:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 13049cf3-b695-33f4-b12d-288d82a8f830 | -6.6146 | -59.9272 | 2026-09-22 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e47ac7c5-a148-35d8-941c-4e2b17bf0f4f | -6.6515 | -59.9258 | 2026-09-22 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a9cb144a-5a82-36d2-b33b-92b2b1b02f5a | -6.6332 | -59.9073 | 2026-09-22 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| fe1da4d7-f741-3bd6-8ba4-d37f35f3b64d | -6.6331 | -59.9265 | 2026-09-22 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 42f5dc31-9c90-3b66-add2-aae5ee7ace43 | -6.6332 | -59.9073 | 2026-09-22 09:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0f7af76f-8fbc-31c0-9a55-e802eea983d3 | -6.6331 | -59.9265 | 2026-09-22 09:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 15ba7816-befe-3595-be12-1112b5d9cea1 | -6.6515 | -59.9258 | 2026-09-22 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7153543d-52f1-34df-aa30-6ec6fb78b6c5 | -6.6146 | -59.9272 | 2026-09-22 09:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f6d39365-6b38-3c8a-bd68-2838a9b2f8bc | -7.03 | -44.67 | 2026-09-22 09:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| beb088f8-326c-3313-adda-1ca1d287c74b | -12.8526 | -50.91 | 2026-09-22 09:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 18b4ef33-4400-324a-8e8b-8e7a39f5375b | -12.8722 | -50.8862 | 2026-09-22 09:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5d2d9d12-57dd-3a96-8eb5-f31a1aee456a | -12.8718 | -50.9076 | 2026-09-22 09:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 405.8 |
| 7dd3d6e1-8eea-37f9-9608-a5e0bbe84cc7 | -12.8715 | -50.9291 | 2026-09-22 09:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.5 |
| ae41b81a-2be0-35e1-888a-f3d23c13ce11 | -12.283 | -50.7011 | 2026-09-22 09:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8d006514-f549-32f0-8811-aa7f5eec312e | -12.8526 | -50.91 | 2026-09-22 09:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 3e1b8c67-511d-3b37-8b1d-d08e3fabef98 | -9.6108 | -43.9477 | 2026-09-22 09:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 63f4e9e0-44ad-3a68-a016-e5a400257d98 | -12.8718 | -50.9076 | 2026-09-22 09:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 759501e8-66cb-3e16-a40f-43694e4316d6 | -9.6298 | -43.9453 | 2026-09-22 09:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 0cb7988d-1f19-3bd5-b26c-68dc9dd2ade7 | -12.8718 | -50.9076 | 2026-09-22 09:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 08569a86-4148-35bf-a19b-2ba1685bbaa7 | 1.54788 | -55.8592 | 2026-09-22 11:42:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cc2290f3-03f2-3a23-9944-3d1235c4ec0e | 1.53601 | -55.90148 | 2026-09-22 11:42:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ba0a818f-f2a2-3710-a492-be0fd98b64e3 | -7.46786 | -45.48114 | 2026-09-22 11:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 508a1196-412a-30f4-806f-06ab0e8fb8aa | -8.09191 | -44.37186 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 31024d8a-4d51-3819-ad24-55a240f3a68a | -6.44569 | -48.45867 | 2026-09-22 11:45:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0906192a-b90a-30c2-bec2-740084b5bc01 | -8.35363 | -50.86883 | 2026-09-22 11:45:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c52a869b-c4c5-3708-87e9-c9901719e722 | -8.4508 | -45.81925 | 2026-09-22 11:45:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 63cc011e-e29c-3c92-a0e0-41af474c0965 | -3.34625 | -42.77094 | 2026-09-22 11:45:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f468c857-9321-3fd2-a77d-f2e80ac8ab6e | -3.68793 | -42.95786 | 2026-09-22 11:45:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bec0ae3d-55ef-3a27-b7b8-244ec4bc3d78 | -8.13718 | -46.82593 | 2026-09-22 11:45:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb7eab67-721b-39fa-8c2a-950bdbb6d0e9 | -3.97124 | -43.10973 | 2026-09-22 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ab437ad3-be43-3a01-8c54-af2b5e186d49 | -9.04077 | -44.9199 | 2026-09-22 11:45:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3c48d81d-ef41-30f2-b665-57ea734e6924 | -8.09241 | -44.36652 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d84c032d-a760-396d-8d9e-5496bc1ae8f4 | -7.02032 | -44.65492 | 2026-09-22 11:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c32ffb0a-6ebb-31bd-9188-dd57ce53c74e | -9.24098 | -46.17175 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 576ef391-743f-3a41-baf2-89bd2dcae1eb | -6.12052 | -44.67426 | 2026-09-22 11:45:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 80409f02-3f70-34fe-889d-ce26192ca354 | -6.20475 | -47.50902 | 2026-09-22 11:45:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d341c6dd-4848-30a0-bc48-3ffc9e7b77e2 | -8.45214 | -45.80941 | 2026-09-22 11:45:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 985eadf3-16ce-3367-9304-c5d26cfc5870 | -10.10013 | -46.08461 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 128792e1-efe0-33cd-a765-c393fe1dc094 | -6.11586 | -44.6784 | 2026-09-22 11:45:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 994129f1-97a0-35cb-8f3e-abcd34dded3f | -8.2567 | -55.25984 | 2026-09-22 11:45:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8b304dde-8d01-3b82-b87b-d6c61910bb03 | -10.25388 | -45.48046 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a7cd623f-d940-3c07-bc76-7b93a1600990 | -7.63027 | -45.0788 | 2026-09-22 11:45:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 77f56eb8-829f-386b-bdc7-64b592620eeb | -7.03157 | -44.64526 | 2026-09-22 11:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 45282c73-76ba-3882-9b80-150a9ee46266 | -5.82548 | -44.13169 | 2026-09-22 11:45:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 74148b1d-14fd-3e7a-839f-d8f0a4703689 | -5.80708 | -47.77035 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fd048c8-4727-336e-8550-1906c8bc4117 | -8.10336 | -44.4385 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 779c4a1f-eed9-386e-9568-d77068c4cbfa | -8.7999 | -44.27131 | 2026-09-22 11:45:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 760531ba-dbb7-3324-a572-cc6f652380f0 | -9.53036 | -45.38877 | 2026-09-22 11:45:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |


[Clique aqui para ver as próximas entradas](README123.md)
