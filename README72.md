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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37ff2744-d173-34f3-bc31-94f34c65bb2e | -2.93997 | -52.57177 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e1617f9-06f8-363c-9686-2f9a711ed46a | -2.93985 | -52.98178 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54779fd0-43fd-3a3b-b768-2fcb8dcd05a8 | -2.93957 | -52.98239 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2990efd6-66d4-3872-8fad-aad247e0d1e6 | -2.93922 | -52.98568 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbbc0333-ced3-3a81-991d-849512dbb573 | -2.93895 | -52.98628 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c19cbecd-bfc4-3e54-98f9-ea76c306939e | -2.20689 | -53.68968 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a01e007-6bc0-3ed7-bc36-97dd483e9198 | -2.19319 | -53.72775 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8be7d7e7-51a6-386c-8547-51fdebeb5057 | -2.19248 | -53.73214 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2aef8cf7-eb23-3cb8-a157-250e0d9e7661 | -2.18949 | -53.72719 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bc22592e-5c1d-3dc5-8cc5-82b2186f9ad7 | -2.18878 | -53.73157 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a8a7b8d-93c4-3ab9-9a3e-6969c9d87691 | -2.09696 | -54.59693 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9878f1ad-fd3c-36bb-a634-c5e6fee003dd | -2.09305 | -54.59631 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9e157bf-d630-36f6-a3d2-5e3d8d263009 | -1.60605 | -54.77785 | 2024-10-26 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55e4a784-20b8-3ab1-b504-4b94ccebc948 | -1.34753 | -54.61231 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1016c252-810e-380d-a671-922979028025 | -1.34359 | -54.61165 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f75e48fe-cfd3-38aa-b3fa-a7e8cb71e6dd | -1.33965 | -54.61101 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 641789aa-2fc7-3e70-8f7f-a69c264e78ef | -1.18727 | -54.20155 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81cefc8d-f532-3a16-bf54-d6baece60094 | -1.18514 | -53.67162 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1898cd7a-c8e4-3c84-97ba-bd53d5239ab0 | -1.18444 | -53.67611 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 461a495c-1df8-3263-998a-8b6d99a17f9c | -1.18208 | -53.66671 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e806fed-71db-3517-898e-caf02a2c2e1b | -1.18139 | -53.67117 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9d31ad-1200-3abd-8c4c-e4c19bdbf83f | -1.18069 | -53.67566 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f70374c-64fb-38e7-bba2-463ed2e28e1e | -1.18029 | -53.9007 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ec7554e-b844-3783-8926-dae639be20f6 | -1.17954 | -53.90531 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bac4c561-39c0-3ef4-aba9-d612f0a3a474 | -1.17834 | -53.66621 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7310ec4-4c37-3a94-ba3a-bc6e6240d21b | -1.17764 | -53.6707 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2092d1b5-7f23-3f59-8f0c-0f7378266ecd | -1.17649 | -53.90014 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d608089-cf6a-31c1-a082-d0feb13c3a36 | -1.16399 | -54.09987 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07c2ebf0-ebed-312c-86ae-b95450fe9297 | -1.16039 | -53.65866 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a427bacc-0760-32bb-9445-e845b7924bb5 | -1.13754 | -54.10359 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a458df8d-e227-3179-a02d-d9ecfc686d46 | -1.1356 | -54.1054 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b65f816f-1e6b-302a-8bc1-9a61c0a8d1b2 | -1.1337 | -54.10295 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce217948-0e69-3642-8260-548f51de955e | -1.1085 | -53.41829 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d43b2b8-affa-3453-b243-d744c16b77b6 | -1.07961 | -53.65221 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b05071-6e32-34c0-b382-0c9d4f74b937 | -1.07585 | -53.65175 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece4d823-2d55-3402-bf9a-049f1c2b2003 | -1.07209 | -53.65133 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69003bd9-48d8-36e4-80fd-e83982060010 | -1.07074 | -53.66 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 46696c8d-7ad4-3edd-89d1-4c631eb4214d | -1.07004 | -53.66443 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e18c8247-8f43-33a9-89ee-3081c93f9416 | -1.06933 | -53.66901 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e836674-4c14-39dd-ab80-2671b4570c0c | -1.067 | -53.65942 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a11dc85-0829-36b0-847c-afd5785267f0 | -1.0663 | -53.66386 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3b6791c-e13b-396d-9c87-685aa93e545f | -1.06559 | -53.66842 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff8d41b-ec0e-3f0e-95d2-eff65ec166a8 | -1.06185 | -53.66782 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fb344c6-ab85-3af1-95ef-bc0443b52204 | -1.03648 | -53.5145 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bdbde47-02ca-381c-8110-93946e300fd9 | -1.03577 | -53.51894 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a650fdf-9940-31c8-af39-787ba874751e | -1.03277 | -53.51392 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1daec6-8127-3d6d-abd1-f07abb9285bf | -0.87734 | -53.68748 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba0df8aa-aba6-3925-9424-703e1d9bf277 | -0.87616 | -53.68923 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e6fe8cd-9308-37cc-873c-9f3ee68acb35 | -0.87355 | -53.68713 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923aa08e-8085-3b95-9325-c7a54fe97476 | -0.87237 | -53.68887 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ad750f1-bb6e-37e6-a2c4-a3f7c57e9008 | -3.12128 | -53.71033 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2828e818-68aa-30bb-845c-c73f80ec7865 | -3.11993 | -53.71888 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d37b959-8260-3e61-a79c-c53a8e00e123 | -3.11763 | -53.70975 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 876d665b-9fe9-3023-b4d9-bb23aa1113a4 | -3.1076 | -53.72569 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f8471da-cf15-3050-844c-00733d179635 | -3.10692 | -53.72997 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72245022-74b2-3c85-b19e-d788edbe6730 | -3.10624 | -53.73425 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40592ce9-3527-3eb1-84d4-3f1d456e3aa0 | -3.10463 | -53.72083 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04be9bc6-d161-353c-92c0-e52cacd59b34 | -3.10395 | -53.72511 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23d512ae-0c2d-3b8b-b576-0202d8c5859f | -3.10327 | -53.72938 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c494243a-eb09-3bd0-a9ff-957a715bd8a1 | -3.10258 | -53.73366 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32d03494-bba5-3360-8e57-322557084e74 | -3.10097 | -53.72025 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e323a08-7f76-3950-8ae4-93e848f3758c | -3.10029 | -53.72452 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fe15306-b73c-3b12-9507-a2546cbbea1c | -3.09961 | -53.72879 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cbc3dc0-60f8-3a48-872a-b855b006333c | -3.09893 | -53.73307 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 008d433d-5b48-3337-8b8e-451177db00ac | -3.09732 | -53.71966 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47820ad6-51a3-3fec-ae66-d9a7bf9a2f22 | -3.09664 | -53.72393 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b6ead21-d30a-37bd-afa3-5870b0df542e | -3.09367 | -53.71907 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2c20c91-118d-349e-b617-171d0f95252b | -3.09298 | -53.72334 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dfe3d5a-da43-3a4a-82ae-474d02133de4 | -3.08001 | -53.82796 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f1ed302-1062-38f0-9757-87ea52970662 | -3.07931 | -53.83235 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5514af71-dfb5-32b6-8b93-63521f532fca | -3.07861 | -53.83675 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8586a570-f167-3a16-81c0-abb5a37e98c4 | -3.07336 | -53.82241 | 2024-10-26 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0084535-0e77-32f6-9514-e12ed2272851 | -3.01493 | -54.1386 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37727637-17df-367c-8a23-34604e6de52a | -3.01266 | -54.49371 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a538e4d6-870e-31ee-bf52-95fa29ad1271 | -3.00882 | -54.49313 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99239f5c-eab4-39bc-91a6-2d52dfbfe360 | -2.9929 | -54.54402 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d2d0e6-4bca-39d0-aaaa-8f7c04d1d0df | -2.98533 | -54.59179 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b9adde2-1d4b-3a59-b43e-7328c9fc7c26 | -2.9785 | -54.6348 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3389a7ca-4126-3960-b351-485435a3aab7 | -2.95385 | -54.15379 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e784546e-4ed3-3b8b-a82d-7c72bb84f614 | -2.94287 | -53.70076 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1de45f5-fea6-372e-8c9e-70bfd299cc3a | -2.94218 | -53.70504 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3ead3c-e54a-3670-a807-d5e9e46a0ac7 | -2.47641 | -54.7616 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b601bac-a1fa-3a67-a901-e593098cd75f | -2.47174 | -54.04416 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f41a9164-24c7-3455-8725-4ad3e13084ae | -2.40395 | -53.93415 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecfa4628-7366-3a00-a1d9-c4cc8c5c9c84 | -2.36379 | -54.33247 | 2024-10-26 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f10da2a4-91c7-3372-854c-84addf6d6aab | -2.32537 | -53.9378 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7fd892-9e08-3ad8-8474-e4f848f556a2 | -2.32164 | -53.9372 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8420c8-0dec-3d38-a2de-2213ebcfe4ca | -2.26881 | -53.63274 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 140af4be-07d0-35e0-872a-20f5e7f93d4c | -2.14944 | -54.92281 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1635de22-7b4e-3631-b900-f9b6df0879b8 | -4.48595 | -55.08497 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efa362a9-1318-3f0f-9f1d-181796395408 | -4.48286 | -55.07951 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40900640-0e30-3d49-907d-c736100cf1e4 | -4.48205 | -55.08439 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b03ea21-43d4-3e09-8494-f98be2587a1c | -4.38844 | -55.04224 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21116a3f-66b0-3f60-a692-7dacbaa832ae | -4.38613 | -55.20398 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adc346b6-327a-363a-8f61-2e4294c3f412 | -4.3551 | -55.02709 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c20774be-0897-3c03-a2c9-1e86b9ae9c10 | -4.35348 | -55.03008 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1010214a-885e-3357-bb23-fbde35522a60 | -4.34478 | -55.35867 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4c8914c-b13e-3bb0-8a51-fdb36bd9be50 | -4.34394 | -55.36382 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbbb6163-45a6-340d-99c4-9913718be358 | -4.34082 | -55.35797 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f5ff992-e63f-3a7e-bb6f-abc295d8a2a2 | -4.29587 | -55.09071 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README73.md)
