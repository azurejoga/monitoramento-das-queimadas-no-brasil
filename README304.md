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

## Dados Diários - Página 304

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b947cca8-2549-332f-a9ff-eb9c9b729b18 | -0.09171 | -49.4894 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09b22820-63b3-36dc-ab0b-9066f5ac5d9c | -0.75206 | -49.39848 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ef5bb6b1-8c0e-3e99-8efc-024ff141d5e4 | 1.14607 | -50.03448 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0c8b5db-a296-3d2f-8ff8-367d9baac00e | -0.09693 | -49.4886 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1db6836d-dd1a-3387-a322-2af12542e4d1 | 3.46848 | -51.47724 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdf0e2aa-224d-3eba-bbc6-ef16c8374369 | -0.88277 | -49.30758 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4941745-8841-3d86-bb2d-9093a19321d9 | 3.54326 | -51.2751 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8f2148e4-b5aa-3738-88b2-f12edf8ae9aa | -0.21458 | -49.78849 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce678b4a-d35c-3824-813e-f51fe9f8cac8 | -0.09122 | -49.48624 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2f4e484b-c8b0-37f8-a9eb-47306a9416ee | -0.02898 | -49.6342 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ef3f88bb-c883-3947-ab50-c36abd0246ac | 1.14964 | -52.70376 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de71bb83-dab6-3587-80c3-932b0ef0aea5 | -0.21247 | -49.78765 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94235dc0-15a9-3351-941b-e15fb985d0a4 | -0.88275 | -49.30922 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb3c3ecc-7557-316a-9b4a-fb89029c3aa8 | 0.31381 | -51.11591 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3aef83f1-12b9-323b-b152-434a24a03c33 | -0.09073 | -49.48307 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 127a3f99-cb22-3cc2-abd9-59f03303288d | 1.15728 | -52.73606 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9594dd6b-22ec-3fe9-ad51-4124658fdce8 | 3.73671 | -51.63793 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ac43ec4f-64ef-3187-b435-91a9b429765f | -0.09742 | -49.49176 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6640a5fb-1b68-340d-bebe-8fbea0bfde86 | -0.08453 | -49.47757 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5eed0a9c-a9a2-37b6-b4f2-78b0495eec35 | -0.59703 | -49.43285 | 2026-10-08 16:22:00 | NPP-375 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3c97a20-595a-3bc5-ad46-e669484705c1 | 0.75391 | -51.40114 | 2026-10-08 16:22:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 69892013-5142-307a-9213-5869c879cf8c | 3.73864 | -51.62638 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fe4ef12f-ab8d-3bea-8ba9-a22d2fbbf442 | 3.7897 | -51.59895 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dccf644d-1765-306e-aa56-2295ef3f7c6f | 0.38421 | -51.15527 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| df6babc9-1782-3f28-befb-acbb412b4205 | 0.38484 | -51.15124 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0aacd959-3e2a-3cd9-acdf-ddd95c8117a8 | 0.38293 | -51.16333 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ac0487c0-2ebe-3d4e-b71e-7f218a7a4724 | -0.08502 | -49.48072 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d661f04f-ae95-3b62-b0b6-89cb80f8e81d | -0.7922 | -49.5173 | 2026-10-08 16:22:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5619bdc-3647-307b-a810-046c6f1c41e0 | -0.7573 | -49.39768 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f05bdc96-31d7-362b-a3eb-37a5cdd45526 | 0.3881 | -51.16824 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 24.1 |
| f84a6a8c-f1ab-38c1-9f0d-24efb3dbe39d | 1.15591 | -52.7325 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 172be8ad-aaa4-39e9-994f-cc8b802273c4 | 3.44381 | -51.71849 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1db7e80-a61c-3de7-8db6-8dabac2d35c6 | 2.32441 | -50.87625 | 2026-10-08 16:22:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c608c063-3532-3ba3-a555-c3fadef05b22 | 0.52915 | -50.80624 | 2026-10-08 16:22:00 | NPP-375 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd094846-c579-37e7-a691-5f21c7a1d93d | -0.3817 | -49.94533 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e8bc1f3-bec0-3d76-a361-13253e22987c | -0.20714 | -49.7885 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f080f08c-6e76-3cf4-ba93-e9d55a4fa789 | 2.32501 | -50.87265 | 2026-10-08 16:22:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2036af70-579b-3115-8e76-97da92ea7c32 | -0.59654 | -49.42966 | 2026-10-08 16:22:00 | NPP-375 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c0bfba37-18dd-34ef-be11-04b34d21cfc6 | 0.99118 | -50.02426 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 069d022e-4f21-34c4-8b10-20f8579f7018 | 3.73735 | -51.63408 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 0cc88488-4f4e-3e29-8a86-beeed1e52700 | 3.71282 | -51.5047 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 303c9a7a-98f7-379c-b9b7-a3080cdf2be4 | 0.31318 | -51.11996 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 859a2004-764e-34ac-b769-ba9943b5b073 | 3.5482 | -51.27967 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3f776e74-e80e-3a7a-a050-971fd0389e95 | -1.11687 | -52.25916 | 2026-10-08 16:22:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e76b8289-bf69-3f57-989a-8ae939111f52 | 0.38937 | -51.16014 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0b04dc9e-fd5c-305d-a39a-2918fe9e3b5b | 3.55313 | -51.28424 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e36841ad-f554-3e81-9a7a-d5dc921d0900 | 1.16228 | -52.73325 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bb296f61-295c-30a1-948a-ce253c657677 | -0.7578 | -49.40086 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| baf4d4e4-a880-3e69-8bfb-73fed149cb02 | -0.08551 | -49.48388 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c2361c92-9f90-374d-8693-18334654dd74 | 0.54023 | -50.77299 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69d9d7bd-1cf3-310c-b289-64dcfbc15731 | 1.03534 | -50.02078 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ee00b2ce-a263-33b4-ae14-ba1c72023b8f | 3.70723 | -51.5036 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af1f6d07-84b7-37cc-b416-87a3710d51a4 | -0.02948 | -49.63738 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1b0a992c-8788-3e67-a605-894e14e8354c | 3.55251 | -51.28792 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c464e085-00e2-30ac-838c-eee2fff3d0a2 | -0.90349 | -49.50743 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5695bda2-ec2b-30f7-9840-8a2c9c456f23 | -1.39792 | -53.23151 | 2026-10-08 16:22:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76ad2cb4-f4b7-360a-b073-a8a8183fe020 | 3.74238 | -51.63885 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 15160302-81a9-3dd2-bede-eff950fa658f | -0.09644 | -49.48543 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7dfa46e1-6559-3ae5-851b-a50fd71611d7 | 2.11252 | -50.82838 | 2026-10-08 16:22:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c5a6c9b-c1c1-3a85-81ab-557bc957df57 | 1.15812 | -52.73095 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c9758024-5fbf-3a7c-87c8-00c620709b9f | -10.9762 | -45.4094 | 2026-10-08 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| dcc6c739-a5f9-3459-9c68-be4d820a1e2a | 1.7304 | -55.6061 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4d5afcab-1127-3f97-a395-9fd5d15c3525 | 1.6937 | -55.6263 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 3898d19c-14b9-33f9-9eb8-119b1cf04649 | -3.0447 | -57.4851 | 2026-10-08 16:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 553d76ee-7d04-3926-8b08-31b05d3b3d92 | -1.856 | -57.057 | 2026-10-08 16:30:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| df2b508a-a906-3aa4-aa8f-cb5d998d4e73 | 1.7121 | -55.6063 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 89c5e8fc-21c3-38f0-af33-c2cb06d34ad9 | -12.1545 | -44.7547 | 2026-10-08 16:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 77eb2851-215d-39b3-9362-3e7a79f83140 | 1.6937 | -55.6461 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a3cf14d2-029f-3bb4-8375-8367afb95a6a | -5.7308 | -41.7789 | 2026-10-08 16:30:00 | GOES-19 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| b7a886f9-ac75-330a-8c6f-c5a1658b107a | -11.2912 | -44.8365 | 2026-10-08 16:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 8e2ffe5f-fc13-3c28-b8d2-a86b4de6220f | -3.3912 | -58.0017 | 2026-10-08 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 804ee696-d71e-3365-bf06-e7b1e6bed761 | 3.5448 | -51.2772 | 2026-10-08 16:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 37473c76-7d35-3398-80cb-bd5e34332fa8 | -2.4805 | -56.1072 | 2026-10-08 16:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 83b19612-f80d-39a8-aae5-d6e3a7b2468a | -5.7319 | -41.6589 | 2026-10-08 16:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 233.4 |
| f7e34740-259b-3cd6-833b-68e73d791c0d | -1.4118 | -48.9318 | 2026-10-08 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 64bccec6-37fe-3290-8aae-c02cfa018125 | -6.6901 | -45.3519 | 2026-10-08 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 479f2f37-ba13-38b6-930c-6377bd180270 | -6.6899 | -45.3746 | 2026-10-08 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 7e28e647-c737-3c3b-bae2-ff46005987d7 | -8.9501 | -45.1334 | 2026-10-08 16:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 79b0797e-4915-3145-8bbc-188a3fc9ec36 | -9.4819 | -66.7836 | 2026-10-08 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f5a17449-a726-31af-b199-748a42fcafe6 | -1.3264 | -56.4176 | 2026-10-08 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 430bce03-b502-3c84-9d67-4ceabbab3ae5 | 1.7304 | -55.5863 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9556646e-6aae-3939-8f4d-525ff5b55294 | 1.7672 | -55.5463 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c86db656-0b2e-3f89-9eb6-ab3275982864 | 1.7488 | -55.5861 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9f677fbe-5633-35eb-a9fc-6ecfad086fd0 | -2.572 | -56.1646 | 2026-10-08 16:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 267.5 |
| 7e751cea-af8a-3d0b-b71a-56bc3212e672 | 1.6568 | -55.8045 | 2026-10-08 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0e088fd6-4140-32c2-8aa6-654b5708cf09 | -10.9953 | -45.4068 | 2026-10-08 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| ff0f8df9-b2a0-3dcb-9282-ba7013a96404 | -15.82585 | -40.48447 | 2026-10-08 16:35:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 9548c78f-0eff-3e74-916a-8002d418074f | -15.57475 | -44.52498 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8f0f6150-f588-3bd4-963c-104b86bb1eec | -20.11851 | -42.02914 | 2026-10-08 16:35:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a872fbd7-549a-3c22-8bdf-789e0a73f8c6 | -14.76149 | -39.81379 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| efd4ab82-abf6-3016-a473-f821b79223d4 | -14.42667 | -40.4446 | 2026-10-08 16:35:00 | NOAA-20 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 36d2e1fc-7fb4-3eb5-a695-7d84627e051a | -14.69887 | -41.00763 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d2f533d2-b48a-3ec9-bc71-02b0b68cefe5 | -16.76052 | -40.99724 | 2026-10-08 16:35:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| af09c010-87bd-3c41-b8f7-a05bb03396e0 | -14.39875 | -41.15856 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3539b515-5c30-3ea1-b07c-62df38b7e4c2 | -20.21217 | -40.22523 | 2026-10-08 16:35:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 044011a7-a5ee-3720-8d7c-9d31b386f1ab | -16.21047 | -40.36752 | 2026-10-08 16:35:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 05736ead-ce55-30d8-91a4-fef8463a64bc | -13.95587 | -44.85342 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 310c6ae0-bd8b-33d3-8531-e46bb6d974cc | -15.6577 | -43.26709 | 2026-10-08 16:35:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b887f4cf-f34a-3db9-a9ac-a08f6a76e92c | -23.33188 | -47.86654 | 2026-10-08 16:35:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f90b2e80-a962-3f1f-882c-57c1d81bddf5 | -15.51328 | -42.65276 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |


[Clique aqui para ver as próximas entradas](README305.md)
