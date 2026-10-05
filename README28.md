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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b365c4f-5ddc-3893-9610-f7e2d0eb6a23 | -2.9632 | -54.1497 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6f388285-0d3b-35dd-a098-7e64ddbaa365 | -3.0733 | -54.1871 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 34641268-0f22-34f0-a717-3b143c04de74 | -3.0917 | -54.1666 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| e936b4a8-9d09-3524-a7df-f41dee480951 | -3.4761 | -54.5972 | 2026-10-05 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c1e9c232-946d-393b-913b-93f9ae3cece3 | -3.0917 | -54.1867 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 88cba058-c53c-36aa-bf78-a92b2e6b680e | -2.9449 | -54.13 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aaacceb7-f822-3186-a3a6-d0e687da14b6 | -3.0548 | -54.2277 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0635ebc7-8feb-39f8-a8a2-f5caf5cd3f12 | -2.9448 | -54.1501 | 2026-10-05 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 972d79bf-e85d-3cf7-8e01-37bbedca2b0a | -10.96869 | -45.43036 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13e6fda9-70fb-3e35-bda9-2daaedad8d35 | -11.23763 | -45.24314 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4927ff8e-b81c-3fe3-80c4-3b7ab3189bcc | -12.19346 | -57.10172 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38c81773-2151-3921-84a9-d526a287b102 | -8.67022 | -54.56227 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5f85e08d-8d32-33b0-8ccd-82b4069e4e1c | -9.81448 | -44.79709 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cea80c0b-2483-3993-8fcb-77dc9601f8f6 | -10.7424 | -45.29768 | 2026-10-05 04:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aebdd96-a746-3fcd-b4af-4d652f49b0e4 | -11.68498 | -43.64357 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ac89ff61-9a9c-33c8-b8fe-9fea94727bd0 | -9.8139 | -44.80093 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9e4da9d-bba8-3c53-8d70-546a7c723408 | -8.86372 | -45.38163 | 2026-10-05 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 790aadb4-b741-3007-b32d-7b88f3fb3368 | -11.24512 | -45.24043 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b349d40f-5ef2-364e-8fec-a4baed687a9f | -11.24109 | -45.24369 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f3c22f-345c-3e78-aa50-8a04ed26eab7 | -12.20356 | -57.10751 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20d0ec56-e04b-3181-8444-517ce043e03d | -8.66806 | -54.56017 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 48bb96e9-8f31-385a-a912-c745a2847b23 | -11.76805 | -44.91938 | 2026-10-05 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f5a54e5-31be-3361-8850-be13df0cbc72 | -12.18266 | -57.09951 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 149c07e1-84cf-3136-a505-5cba777dc257 | -10.96753 | -45.41484 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 606583ff-859b-3612-9b75-452faf52d62a | -8.66711 | -54.56559 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| f2162fee-9595-3fb5-b2e1-67434cb3a6b7 | -13.6343 | -44.42204 | 2026-10-05 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43076e99-3c20-33f6-9c53-a9cec9f8fdb9 | -12.18169 | -57.10019 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90cd5e17-4b94-3af9-b3f4-d1ac788b2c00 | -12.87878 | -61.71824 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a4756ee-5aa7-3ccf-8872-f8870694ff0a | -9.81795 | -44.79765 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bece61c6-2681-3942-8c30-f5d4fb1ee764 | -8.66536 | -54.56136 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 651a2e58-7252-3ef5-aedd-ff98d16f0f05 | -10.22679 | -47.99451 | 2026-10-05 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b49fd5f-e8f2-3644-a39c-76347e52d49e | -7.46401 | -55.01566 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8a70c26-f369-3b4c-ba9e-d9930b42c051 | -10.97039 | -45.41911 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91c0c1c8-5dab-3498-afae-b350e69b5b1a | -13.63796 | -44.42267 | 2026-10-05 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 032ec6cf-4dc9-33d1-9dcf-5625ddc4d155 | -7.46827 | -54.99184 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 586dc253-3fac-3ec4-a036-03680cc18453 | -11.71254 | -43.63818 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e652b2d-0a1a-3029-a733-421428472f22 | -8.70557 | -47.5574 | 2026-10-05 04:40:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09fb43ad-e815-3e48-b696-01714c680a96 | -15.57358 | -43.7708 | 2026-10-05 04:40:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e37ced7-7bf7-30ca-9298-754cb453acb6 | -12.87653 | -61.71383 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a51a7e8-51ed-32a9-ad3b-ff351634fddc | -7.47289 | -54.99556 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17001c33-c4fe-3018-a7a5-2fdc714b0442 | -10.96329 | -45.42665 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac2d32f4-94cc-3a86-a4ac-803a99b89871 | -12.18403 | -57.09262 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2369a9-96f7-3196-af91-b19700f4f013 | -11.68191 | -43.6383 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d1272707-dec0-37af-bc81-66049e163ce4 | -12.20196 | -57.11171 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0efc52b2-d617-3b97-8bc1-ae3d02fa5604 | -10.95698 | -45.42199 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 667a44b1-ee7f-3e5d-9eaa-02e72b0f9d41 | -8.67293 | -54.56107 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28da2a06-1dbf-3f69-ba53-b947a741b3e1 | -10.96526 | -45.42987 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 693703be-b85e-3d1b-8f45-89f916aeb860 | -10.96239 | -45.42563 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0b125e3-e866-3575-9210-8ea61cf033cc | -12.88203 | -61.72236 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a5eec27-47ee-3654-bf5e-b07fed7caddb | -12.16246 | -60.75198 | 2026-10-05 04:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c80f718-5995-35b6-8f00-abd899425a19 | -8.66923 | -54.56765 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d1a2ad64-5a14-3355-a557-334bc7d632fa | -11.82738 | -43.53691 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 757396f2-d4d2-3a86-b8c6-b2d441177cc0 | -12.88353 | -61.71545 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce4ff46-e321-332f-8308-59e7a6002bd5 | -11.77094 | -44.92406 | 2026-10-05 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e236ee96-c4f2-32b2-9f8a-629ec5ea345f | -11.68125 | -43.64288 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 24226037-9f90-3f78-8977-33f6b1159a54 | -9.85278 | -44.77931 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57aba9c0-2d06-33b8-814b-2ddd296189a6 | -12.20262 | -57.10825 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d730b61e-e629-3784-98cf-5e7f198d529a | -12.15583 | -60.74999 | 2026-10-05 04:40:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e56c10f0-3c0e-3369-8234-5b6b46a089be | -12.20288 | -57.11097 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e67096e-76a3-32ee-9f75-17b10f436a5b | -12.18874 | -57.09719 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d293d45f-45fd-3867-ac27-8cfc45d67330 | -10.96696 | -45.4186 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 230f83b5-6e79-3088-a55c-72d23f8e281b | -9.83996 | -44.79329 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6902db04-ceae-38bf-9a34-a37a3bfb96ce | -15.49578 | -44.41118 | 2026-10-05 04:40:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1fcf1e2d-fe76-3236-804b-1cee3bf9fc26 | -10.73956 | -45.29331 | 2026-10-05 04:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 318a3180-944b-3b71-a8dc-32bf864f008a | -12.2022 | -57.1144 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7732b961-3a77-3f61-8fa7-72fab61691bf | -13.63367 | -44.42639 | 2026-10-05 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdef11ee-ba0d-35f5-bf71-bb7a68be7555 | -10.96562 | -45.41161 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fb4f5c3-d448-30ec-90f5-ddae3b81daa7 | -10.95816 | -45.4144 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6739438-c822-3dbd-a3fe-06aab9163536 | -11.67817 | -43.63768 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6298ed8f-a796-3764-8d34-90e5a53abefa | -12.87502 | -61.72073 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 157401b7-5f73-34d0-9825-da4a405a8b5f | -12.87732 | -61.72514 | 2026-10-05 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af1d3049-9a37-30c2-aec7-55953490e09a | -11.68564 | -43.63897 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0c9aa60-5dc1-348e-b58e-e9cec982e622 | -9.82489 | -44.79878 | 2026-10-05 04:40:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d7914ec-9d54-3595-850f-7e11b4f2467e | -8.22238 | -50.21599 | 2026-10-05 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59ee7db1-ebc6-3643-8788-a6500d62f95e | -10.95186 | -45.40965 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c4092fb-d1ef-3bfa-8d27-3ada8d3ce6dd | -13.58153 | -43.70551 | 2026-10-05 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 522df366-d2ca-3790-a671-5174b8c53533 | -12.18235 | -57.09671 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bf31ff3-08c0-3600-ad30-8c36565e5378 | -12.18335 | -57.09605 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba92ccaa-1ab4-3bef-8875-505ef2c90b77 | -8.66436 | -54.56679 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bcc88cee-e80c-3770-a0e1-889b87fdae4b | -12.19414 | -57.0983 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af61d436-3d68-36b8-97c5-0366aec9bd27 | -10.95413 | -45.41774 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61537f91-c298-351c-886f-ce9dc17348cb | -7.46348 | -55.0186 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5becf08b-9b9c-3b4e-b318-4cd06f421003 | -10.96466 | -45.41056 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 984fe23e-5625-3d01-bb9c-523850199bbc | -12.05318 | -43.4363 | 2026-10-05 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caa7d82c-88cf-3679-828e-40a32bad6b69 | -7.33281 | -55.03031 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36d4413e-fd0c-3f30-a9f5-c82834aafdb8 | -8.6761 | -54.55767 | 2026-10-05 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 768fe635-3974-3955-bfcc-8f0ff8ee9787 | -10.96983 | -45.42285 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 963ca130-d1a9-38ff-aa4d-a63a520bef64 | -10.95472 | -45.41393 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8074b024-3117-30ec-ad95-03c500cc919c | -16.14314 | -40.69963 | 2026-10-05 04:40:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d8c70ac2-8fc1-345b-9afa-8223d1d296af | -9.5641 | -45.50051 | 2026-10-05 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c28f9a7-8aea-3521-97be-350fe2dd0c03 | -10.95354 | -45.42154 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00810a75-0686-3116-98c0-b1ed76f6cd64 | -13.29844 | -48.37563 | 2026-10-05 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9143280-3a72-31c8-adcf-ceb5dfc757be | -11.7205 | -43.50327 | 2026-10-05 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb33cab3-20d7-398a-9058-3c93c89e936b | -8.27648 | -47.91696 | 2026-10-05 04:40:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e243431-5b91-3df0-a2cb-b453fee917c9 | -9.23466 | -46.68576 | 2026-10-05 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c16859ea-64af-358f-91ee-0f23640ddbdf | -12.85935 | -39.92558 | 2026-10-05 04:40:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46be0199-41e1-3a85-a0d4-655d2c78934d | -12.18302 | -57.09325 | 2026-10-05 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef0d9b6a-d263-3eac-adc0-0bcd0bd70d27 | -10.96813 | -45.4341 | 2026-10-05 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a8dce67-2e8c-3631-9aa5-08528c10d3a7 | -16.67502 | -41.85157 | 2026-10-05 04:42:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0890ce80-9ae1-37df-a87b-0b92cbdae43d | -13.51041 | -61.12598 | 2026-10-05 04:42:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
