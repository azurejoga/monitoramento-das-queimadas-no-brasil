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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c6d7b4-b54a-35c7-9aa7-d04182e29b3a | -17.3643 | -42.6284 | 2025-08-29 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b2f8f383-c142-302c-a973-cc2e9bacedda | -12.4345 | -63.9173 | 2025-08-29 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 8f28e7a1-4a62-3363-8b07-9ea3a66696c5 | -10.3624 | -57.8258 | 2025-08-29 01:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| af8eef0c-5b6d-30d2-bfac-e04c094ba60e | -7.0381 | -44.364 | 2025-08-29 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3cb906b3-c76d-3cd3-8720-b080f5045335 | -12.4156 | -63.9183 | 2025-08-29 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 75e142c6-621c-39db-90d7-79887923f5c3 | -5.6268 | -45.0025 | 2025-08-29 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 623c908f-8926-38c0-86cd-130dbd2f5cc3 | -9.7915 | -64.265 | 2025-08-29 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7861c489-fe9d-3f9b-bb08-d5bfa6d7f1df | -6.5546 | -43.9221 | 2025-08-29 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a615711b-223d-39b1-95cd-aefea80f36c9 | -13.1833 | -45.3098 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 58fbfce4-490a-3f50-892c-1fbb9f4a9810 | -3.4254 | -49.0517 | 2025-08-29 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c4953faa-4c33-3ada-a7be-a8232bf0d1d7 | -6.5358 | -43.9237 | 2025-08-29 01:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e57bb333-3209-3a8a-bb25-e60cbe143a2a | -9.773 | -64.2469 | 2025-08-29 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 261.3 |
| ef254769-7735-305b-a177-ed50326e3ba2 | -18.1257 | -50.2363 | 2025-08-29 01:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| fa289559-c187-3acf-8cac-2ad71f7c367a | -13.5386 | -46.8775 | 2025-08-29 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 29a8e4ff-c233-332f-b635-f3a221b95002 | -12.9961 | -56.9201 | 2025-08-29 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 079d4f7f-71b5-379a-b296-3d9bf1fc7fd6 | -18.1457 | -50.2326 | 2025-08-29 01:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 61c76db9-639a-339a-b347-34c1f0481579 | -18.1252 | -50.2586 | 2025-08-29 01:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 1782dc70-02d8-317b-91d6-01671535629f | -5.6266 | -45.0252 | 2025-08-29 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| cb94c735-1484-381d-b135-737e2a8b5ce8 | -8.1758 | -61.3755 | 2025-08-29 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| da604e29-862e-37b7-ada5-c35d04332998 | -18.1052 | -50.2622 | 2025-08-29 01:10:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9400c776-f0cb-3bb3-b21a-894f5edfe876 | -6.1672 | -47.2858 | 2025-08-29 01:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 38ea4aec-2700-328e-8bfc-1040058bd7d1 | -13.1842 | -45.2633 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0251f736-bfc5-3920-9daa-40982c23c601 | -6.7074 | -49.4561 | 2025-08-29 01:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| d27216fa-e4f6-31c7-bfcb-1e270890c61b | -13.2027 | -45.3066 | 2025-08-29 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 969a6b28-b366-39c5-b9ad-e634fad3f3a0 | -9.4432 | -60.5692 | 2025-08-29 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b72bf214-f2e3-34b6-99d5-6ac5cc4f3344 | -13.5584 | -46.8517 | 2025-08-29 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 65561863-8bc0-3394-95db-361db13b1abd | -8.1944 | -61.3747 | 2025-08-29 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1489e631-7630-37ad-9d71-e842b010dce5 | -13.558 | -46.8745 | 2025-08-29 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| deb83ab0-1cd5-3c04-ac77-34f5d894d3c3 | -9.426 | -47.6605 | 2025-08-29 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2f1eaf2f-e6d6-3de4-ae5d-3d8f32c8c6ef | -6.9683 | -59.3362 | 2025-08-29 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cc90f9a9-131e-3432-a187-890a131c9eea | -9.2178 | -60.8689 | 2025-08-29 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2043836f-9354-3b03-ba1d-e086cb66e637 | -18.1457 | -50.2326 | 2025-08-29 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2eb904be-d2c4-35cf-9023-0af7388bee72 | -18.1257 | -50.2363 | 2025-08-29 01:20:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1392e503-dc16-3bc3-8bbe-d074a96bb606 | -9.4263 | -47.6384 | 2025-08-29 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 815d8be9-246c-37ab-84b3-cd6c10ee86ba | -14.3299 | -53.3108 | 2025-08-29 01:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 260badf3-7119-3a0d-8012-938e57480347 | -8.1944 | -61.3747 | 2025-08-29 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f3d8d519-6377-320b-ac07-c1270b4c25b9 | -13.1837 | -45.2865 | 2025-08-29 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 049efa59-b58e-3375-a351-d9ca8dbe64f0 | -6.7074 | -49.4561 | 2025-08-29 01:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 2b50db4f-991a-3f35-adba-9e9da09aedd8 | -9.773 | -64.2469 | 2025-08-29 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 245.1 |
| a1a450db-dac2-3af9-b8dd-187c9aee5901 | -3.4254 | -49.0517 | 2025-08-29 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4c882d86-5a9e-3b40-92ee-db6875e55aee | -9.462 | -60.549 | 2025-08-29 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| f4ec9544-c37c-3f57-9a26-5d80f1685352 | -13.2036 | -45.2601 | 2025-08-29 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ea2d7fa3-7238-3e50-9521-e173e36420f3 | -8.1758 | -61.3755 | 2025-08-29 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| ccb25bc6-aea1-35df-a8a8-51db110308b4 | -13.2027 | -45.3066 | 2025-08-29 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| dcda2a43-4a17-318f-b8f6-8dedee1b8f1e | -9.4449 | -47.6585 | 2025-08-29 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| e5009997-0cb6-3645-b63d-439df4888338 | -5.6266 | -45.0252 | 2025-08-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 49456652-3844-32f4-a638-382005c0f781 | -6.5358 | -43.9237 | 2025-08-29 01:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 97e93e00-8f2d-3ebc-ac63-cc88ec819197 | -9.4452 | -47.6364 | 2025-08-29 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 01c50162-7c62-3598-a58c-d3aa9f3bbc3c | -12.4345 | -63.9173 | 2025-08-29 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 136.7 |
| d07cdd8b-f4b6-3ed2-93b2-ffeaf28adc9c | -22.6756 | -46.8439 | 2025-08-29 01:20:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 99d45962-f20c-34fc-9573-891d54624754 | -12.4344 | -63.9364 | 2025-08-29 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 67272622-4706-3d29-b21e-77d9e8a0c6a3 | -9.4433 | -60.5499 | 2025-08-29 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 75bd14d8-e4a0-37c5-b6d7-a161a9854478 | -6.9867 | -59.3354 | 2025-08-29 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 06b517d6-2b35-330b-a564-63e5741e7bef | -13.558 | -46.8745 | 2025-08-29 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 96eac613-9cba-3d90-815c-21521a06f531 | -13.1842 | -45.2633 | 2025-08-29 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0bfa456c-4be6-3a20-9bae-5a57585c2a22 | -5.6081 | -45.0038 | 2025-08-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b7c19212-cc73-33a4-8146-b8df8af7f865 | -6.5546 | -43.9221 | 2025-08-29 01:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 1ce0c145-8ff6-3887-b00f-41b1df8ad4bf | -9.7731 | -64.228 | 2025-08-29 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 49d95a26-d39b-31fa-a24f-1b1d9289fa51 | -6.1672 | -47.2858 | 2025-08-29 01:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2c1b14e4-3850-32b1-9490-c7e529ff4139 | -10.3624 | -57.8258 | 2025-08-29 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8d834cef-9cb1-3509-bc60-8b3acf42b71c | -6.7072 | -49.4774 | 2025-08-29 01:20:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e2c9e207-2b20-387f-aa82-2e445842640f | -13.5386 | -46.8775 | 2025-08-29 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| bd2daeb9-6436-324b-98ad-999f1db41e78 | -13.2031 | -45.2834 | 2025-08-29 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 240.7 |
| 17b1648f-de39-35e0-b1da-f4907b729355 | -9.7728 | -64.2657 | 2025-08-29 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| e59b3ed6-a036-34c9-a400-56bb269d05fe | -7.0569 | -44.3623 | 2025-08-29 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 32078223-1ad3-3d66-a9ce-e500c6d68619 | -5.6268 | -45.0025 | 2025-08-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 50c35ce8-deb4-33bf-a547-74923b766f3d | -18.1252 | -50.2586 | 2025-08-29 01:20:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e609c066-820e-3595-90b5-be153df2fd27 | -5.627 | -44.9797 | 2025-08-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 792580c0-ba58-3c21-bb6b-61b10e361e52 | -9.7916 | -64.2461 | 2025-08-29 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 89c46b7c-8a77-3d9c-9c6a-66b43221ede4 | -9.4432 | -60.5692 | 2025-08-29 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 654c8926-f53c-3f7e-bf5d-ed64f65453df | -13.5391 | -46.8548 | 2025-08-29 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 863f46a8-7c8e-3be0-b2aa-6f4746ecb4f4 | -7.0567 | -44.3853 | 2025-08-29 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0d0fda98-0c9a-3fc7-a4aa-43ac38e59943 | -17.3442 | -42.6333 | 2025-08-29 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 421ccb40-3f05-32fa-a672-159afd493cce | -9.426 | -47.6605 | 2025-08-29 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 270ce6eb-9e72-3e3d-a137-b27b53b4ded0 | -12.4156 | -63.9183 | 2025-08-29 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5d40e717-8ba3-3076-a6c0-25af811c8689 | -10.3812 | -57.8245 | 2025-08-29 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5c14d1c8-3615-3a25-b15e-c2350e7de4f5 | -18.1452 | -50.2549 | 2025-08-29 01:20:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 558a4b60-daed-3f2a-b3eb-738e84bd2622 | -12.0976 | -44.717 | 2025-08-29 01:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6a97b116-c6cf-3da5-a41c-2cda1ca7b576 | -12.9961 | -56.9201 | 2025-08-29 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| fb328438-2d63-334a-8fb5-447fe73e70a9 | -9.7915 | -64.265 | 2025-08-29 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1d1234c6-b07e-330e-a27b-83d309905e30 | -9.4618 | -60.5682 | 2025-08-29 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| d3a02c51-a9b0-36e1-8a05-bcac76f8bc10 | -6.9855 | -59.334 | 2025-08-29 01:21:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad1002ef-6348-31be-aa76-0f5652df6703 | -9.1744 | -60.7756 | 2025-08-29 01:21:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ddffe95-5b6b-36cc-b321-962f793a4fe2 | -8.5457 | -70.732903 | 2025-08-29 01:21:00 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d2fcac71-33c7-3fd8-80cd-5b0dac5ea148 | -10.365 | -57.815102 | 2025-08-29 01:21:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 701d9b06-8172-3caf-b09e-a0c5c437774b | -8.6961 | -62.474899 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24e7aa7f-baec-3f53-b610-e703142463cb | -8.1401 | -61.199299 | 2025-08-29 01:21:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90593da1-9ae5-37e3-b409-7683c132c8af | -9.0087 | -64.151703 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8557c22c-727f-3b1a-b516-dda60c67d5f9 | -8.2842 | -61.4174 | 2025-08-29 01:21:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 897a9a17-8803-395b-ad0f-ae8edd983b28 | -12.4372 | -63.907501 | 2025-08-29 01:21:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea5b7f5-3ed9-3686-8af9-f2edddecb5d8 | -11.3754 | -63.270199 | 2025-08-29 01:21:00 | METOP-B | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| caedee22-a6c5-3617-9683-86e8e98c1ffe | -9.1156 | -65.7742 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 143d4318-9e38-3537-9da3-323925fcf436 | -28.709801 | -55.586201 | 2025-08-29 01:21:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2e79b527-2ba6-32ac-9dd7-2e92df1a5b96 | -11.2218 | -55.060799 | 2025-08-29 01:21:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6159474b-7705-3c5a-8a13-d252072c4f43 | -8.5856 | -63.923 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91d50699-93eb-3c8e-980d-eedeb5a1b1fd | -9.7902 | -64.234398 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2504ba95-b686-3ad5-a5a5-9cf32a054999 | -14.3313 | -53.299702 | 2025-08-29 01:21:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 103a3cca-fafc-3feb-9de5-fe85fbcfbab8 | -9.1399 | -65.2827 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93b0bfb7-4951-317c-9750-dec1b27e9eab | -9.7836 | -64.250702 | 2025-08-29 01:21:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77798656-a050-395a-98e5-057c9fb528e6 | -8.957 | -65.940498 | 2025-08-29 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
