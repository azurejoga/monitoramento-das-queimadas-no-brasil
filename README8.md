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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4f7e1e2-31a8-34eb-8474-5a2fea3ef2fe | -12.2723 | -44.62 | 2026-05-09 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 288.6 |
| c3608082-8ef3-3dc4-8aa7-0b69c9964d89 | -9.4068 | -50.7059 | 2026-05-09 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3b4df044-bcc0-35fe-b2e9-d3c5c7aeb5d2 | -12.2911 | -44.6404 | 2026-05-09 13:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 29eb00a9-cb4f-3bc8-bb4a-dc9774756900 | -9.4071 | -50.6847 | 2026-05-09 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0ad25458-c30f-3b26-a43e-c5b459c26dbe | -14.2118 | -57.4299 | 2026-05-09 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| cd7cb507-9233-3786-a833-d8b3492597c2 | -9.4071 | -50.6847 | 2026-05-09 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e5666bc8-871d-360f-a805-1e4fba9c6ae5 | -12.2718 | -44.6434 | 2026-05-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 214.5 |
| c78cc6b5-f59c-32d9-b32a-d3d1f2a7c681 | -12.2911 | -44.6404 | 2026-05-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e99a2aba-4cec-3018-868e-2326999591f2 | -12.2915 | -44.617 | 2026-05-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 169fd679-270e-32bf-98c5-013808f812d0 | -12.2723 | -44.62 | 2026-05-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 401.3 |
| 3f125ca3-7327-34da-8600-2bbd620337bb | -9.4068 | -50.7059 | 2026-05-09 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| bbbb6a8d-8997-34fa-805d-3b133de030a7 | -14.2118 | -57.4299 | 2026-05-09 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 7d09c19d-830c-3979-b91a-137c0cf02757 | -9.4071 | -50.6847 | 2026-05-09 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 92f72879-6530-37f4-acd7-5bc2d7379722 | -12.2723 | -44.62 | 2026-05-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 637f279f-8bc8-376a-8bd9-25bc44f43bc2 | -9.4068 | -50.7059 | 2026-05-09 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| ff44e9f9-04c6-3a12-afb4-5fc8e05e3a45 | -12.2915 | -44.617 | 2026-05-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| ce6aa0a6-f0be-372b-ac93-02ff9b18a14e | -12.2718 | -44.6434 | 2026-05-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| a381ad76-2ada-327f-9003-ca9803e1f2bb | -12.2911 | -44.6404 | 2026-05-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 6e37afe3-5c28-3387-b502-c9f962024f00 | -9.4256 | -50.7042 | 2026-05-09 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| cccf2822-d1c6-3082-8b03-b251b3e25390 | -9.4259 | -50.683 | 2026-05-09 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5f16f8b1-904b-3f78-97f2-957b67182910 | -13.9926 | -56.6234 | 2026-05-09 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 32e08b11-347b-3826-a8bf-fb13d63ee605 | -12.2915 | -44.617 | 2026-05-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 850015c9-22ad-337b-b27b-5a3a6a0c6ad2 | -9.4259 | -50.683 | 2026-05-09 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| cbc3e7bf-0324-3db6-9bcf-26e709db5364 | -12.2718 | -44.6434 | 2026-05-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 88c9466a-5f1d-30f2-aec4-d901d9f1ae67 | -9.4071 | -50.6847 | 2026-05-09 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| b2a51fba-f3a1-31e4-ba0e-04d022ccc42e | -12.2723 | -44.62 | 2026-05-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 3b96a1c9-3240-377a-9e66-83e3da4cda32 | -12.2911 | -44.6404 | 2026-05-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 995ab251-c181-3138-9bca-1d5cd120aae1 | -9.4068 | -50.7059 | 2026-05-09 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| ac494f54-23eb-3d72-b3b0-7e02f4de0492 | -12.2911 | -44.6404 | 2026-05-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| bf4f8d70-1c3d-3093-8f73-04663c31ded7 | -12.2718 | -44.6434 | 2026-05-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| bc870b48-d7b1-3295-9668-eeea1b33f179 | -13.9926 | -56.6234 | 2026-05-09 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 07256219-9df6-3e40-84ab-f56b90e4d9c7 | -9.4259 | -50.683 | 2026-05-09 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| cd3a7a9f-6206-3c3a-9426-14501e5f478e | -12.2915 | -44.617 | 2026-05-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 92cda52d-ce94-3eee-9f2e-000cfbd4265f | -9.4071 | -50.6847 | 2026-05-09 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e0a3708f-f54b-37c3-be60-bded9f170bd6 | -9.4256 | -50.7042 | 2026-05-09 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c0dbc66a-f24a-358a-b582-66c8b28cf815 | -12.2723 | -44.62 | 2026-05-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 09807ee6-5c85-37ec-bc4e-437b8601f4c4 | -10.3443 | -46.9142 | 2026-05-09 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 050474a0-51db-3c7c-a55f-70b5c8ce7fc9 | -9.4068 | -50.7059 | 2026-05-09 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f0dbd7e3-86ad-3f35-996c-4e9f9fec6ed3 | -14.0118 | -56.6215 | 2026-05-09 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0cef4da5-fbcf-3280-b165-9240ec1bb360 | -12.2718 | -44.6434 | 2026-05-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| e12b7e33-0bc3-39d4-876b-c8ae8af001bc | -12.2911 | -44.6404 | 2026-05-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bd5b91da-168c-3451-a398-cc3e137affef | -9.4071 | -50.6847 | 2026-05-09 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0360c419-5138-349d-bbb0-d168c22b2e91 | -9.4068 | -50.7059 | 2026-05-09 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 04634e7b-cb78-39f8-ab90-1ea0b4818e13 | -12.2915 | -44.617 | 2026-05-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| ba1ad8cf-8896-3825-b8bb-238cd5297f51 | -13.9926 | -56.6234 | 2026-05-09 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5c30a30f-05cd-3bf8-be65-3af9ca1f1c39 | -12.2723 | -44.62 | 2026-05-09 14:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 094e2f7c-272e-30b7-95d5-34d84a31029f | -9.4071 | -50.6847 | 2026-05-09 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8a08a2d1-3363-3526-96a7-ae42311b5ec5 | -9.4256 | -50.7042 | 2026-05-09 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4ba93d19-81ee-3939-9e94-49d4c613efb6 | -12.2915 | -44.617 | 2026-05-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| aa067b46-5176-32f2-a537-a144c7baef16 | -12.2723 | -44.62 | 2026-05-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 20a12597-4993-3876-b584-45d20b6d9ac4 | -14.0115 | -56.6418 | 2026-05-09 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 92e1bd33-28f1-3ea7-9254-915301d92fca | -14.0118 | -56.6215 | 2026-05-09 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 63bda4ff-25af-3d83-8b30-00e63d54702c | -12.2911 | -44.6404 | 2026-05-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| dfdbaf13-dec0-3dcd-8f82-89b604c89b8b | -13.9926 | -56.6234 | 2026-05-09 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| af5dd5b8-8886-383b-9734-308d08bf697d | -12.2718 | -44.6434 | 2026-05-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 3bc152c0-f486-3479-aae9-d61db57a1140 | -9.4259 | -50.683 | 2026-05-09 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 05373e3b-2f5d-3ee0-a104-fbe739603e22 | -9.4068 | -50.7059 | 2026-05-09 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |


