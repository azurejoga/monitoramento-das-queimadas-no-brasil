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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f108b7cf-7a40-3d0e-b4a7-a75dc81a827c | -12.72248 | -62.94155 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85480922-467e-3313-9e4d-910db35b7700 | -12.71267 | -62.93609 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 286b9ae8-4e1d-36d6-8a49-e3131988e464 | -12.71038 | -62.95147 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9db585fb-b93f-3eca-9406-3af7ec9b8de3 | -12.70978 | -62.9317 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc563a0-ade0-3938-b6df-1d3bef0328e9 | -12.70921 | -62.93555 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e2327b-222d-37c0-954b-213a4a844fcf | -12.70632 | -62.93117 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc87b88-41fd-3eee-8e29-0b43bce42970 | -12.70575 | -62.93501 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c407738-2ecf-3be1-9c32-63d399997f0c | -12.9878 | -62.68124 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dc660e1-4a9a-3508-a1eb-d83978521218 | -12.98489 | -62.67675 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b271c69-ba5d-305b-a32d-fa4974884527 | -12.9843 | -62.6807 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 967c875d-92b1-3fd8-8253-aa28588cd794 | -12.98079 | -62.68016 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62cca41c-41a0-3012-8f86-b63b1604194a | -12.98021 | -62.68412 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 634d9420-d051-3ba7-841e-91dc1f736df5 | -12.97671 | -62.68358 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bdd36ab-ea92-3201-8ec2-e1d400e9c366 | -12.97612 | -62.68755 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56532d7a-2990-3a4e-bdb0-528de62864f0 | -12.97609 | -62.78413 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8965e9e8-4c9b-36d7-8b92-e1c5f3e1ad0a | -12.97262 | -62.71122 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d17e35-9f78-3c22-a961-7b9dc8df5f58 | -12.97262 | -62.687 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba76fdb6-6c51-3ec4-b3c0-dd6a34946864 | -12.9586 | -62.66056 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd63bcea-9833-3163-910a-be77407527b6 | -12.94202 | -62.47963 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5f86a8a9-dd5e-335c-a86e-e1c1239f7aa6 | -12.93909 | -62.47506 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c623c3ee-65b4-3fad-a4bf-556776d8aaa9 | -12.93849 | -62.47908 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1d29c29-9a81-3673-af5c-15da36503a84 | -12.93083 | -62.48202 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96de7e7b-d6fd-3a85-955f-f09dd0542686 | -12.93024 | -62.48604 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419ce778-25e5-39b9-90ac-bbd7a74f130b | -12.92784 | -62.50212 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8d7657-043a-30f7-bf76-8564f449889b | -12.92491 | -62.49755 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3be85031-c873-31bf-ae17-1c293b9eeece | -12.88648 | -62.7793 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 005bc960-5a99-3b86-b707-8ae640186692 | -12.88241 | -62.78268 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df98d89-3f53-36a3-96d6-1f87f45400e6 | -12.87893 | -62.78213 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62bad651-8766-3a70-80db-9f2cd94c3e56 | -12.87432 | -62.44874 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4d7c81d-9511-3a82-8f77-633de9e77142 | -12.87427 | -62.78942 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 037d546b-0209-31c9-9151-8210d77c6c8c | -12.8702 | -62.79279 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 279b819b-ffc8-3c39-a119-8ec0d2cfc4c3 | -12.84814 | -62.79737 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6592b00-dfac-307a-90da-a4e1d4a51a62 | -12.84756 | -62.80127 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be50c751-2d6f-3943-bcb0-315ad7cbe430 | -12.84408 | -62.80073 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9469e548-5241-329b-ad69-42711a42a024 | -12.83711 | -62.79965 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8c0f047-875f-35f2-a48a-dbb5eb5fd661 | -12.94263 | -62.4756 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 60a1f09d-00d4-35a1-9bce-de1ff181ac4b | -12.9379 | -62.4831 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6d8fa87-7fad-3eea-898f-ea4611c02c92 | -12.93496 | -62.47854 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d005fe4f-1a4f-34f2-8744-f37525ebfe20 | -12.93436 | -62.48256 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0592a0e4-2421-3193-aa03-fd294c7aa7b9 | -12.92431 | -62.50159 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616f3fe2-9ed4-3a6d-be31-8d5274c99c9b | -12.88492 | -62.45036 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a78fed28-eef3-359a-b363-81ed6fd127aa | -12.88198 | -62.4458 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc505b94-880f-3f2f-9532-109389b4a5e5 | -12.88139 | -62.44982 | 2024-10-06 05:36:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f8d0b4e-8212-35eb-87de-10066ff82ce4 | -12.71441 | -62.94817 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 038fc130-9ed7-342c-9378-d2be082a2121 | -12.71384 | -62.95201 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5340f521-eead-3c00-9852-16c59efbd782 | -12.70749 | -62.94709 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16a77501-e832-33be-acfe-d6a89d405753 | -12.64971 | -63.09851 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7308cef1-ee9c-3263-8080-2e680df390df | -12.64627 | -63.09798 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a50c85b-d10d-3fa7-92a6-3eb6bd87a1bf | -12.64372 | -63.09771 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0afca2d4-60e3-3977-8f0b-14dd2a4d6082 | -12.64283 | -63.09744 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a178c2-2aef-3e52-8461-0316a831afc4 | -12.64227 | -63.10124 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea5fff10-05a0-3d88-9765-ed6eba964c31 | -12.64028 | -63.09718 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e7faf4d-e94f-37d6-a184-966ba6bd6b9f | -12.63626 | -63.10043 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13114a75-80b3-3ff5-8002-07063f50cd76 | -12.63282 | -63.09989 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 689f754e-02ca-35ee-a1e0-3c26ebcc1542 | -10.27333 | -63.14532 | 2024-10-06 05:36:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f80e4de-dc71-37b0-a077-ec815d247c5e | -9.61305 | -64.05023 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e54044d-a7a7-3fea-9913-b8442d79ad03 | -9.6125 | -64.05373 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c33af01-03c5-3dcb-85d4-03c8b985d12b | -9.58175 | -64.22821 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd6dadd-2910-3378-9104-ed05b7dd0ba9 | -9.57897 | -64.22418 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c37942ce-da91-3516-b8ad-466257f7beb6 | -9.57842 | -64.22768 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f5274a-a268-358e-8eed-b8589efbad91 | -9.5762 | -64.22015 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b53cb891-36e4-3acb-be12-54396a53a396 | -9.57565 | -64.22366 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c1d9fc2-fd30-3671-8690-f6b3aa85d515 | -9.5751 | -64.22715 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48534e2d-df94-38d4-82f2-5689ccb2518a | -9.57287 | -64.21963 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a723451c-d1c1-3d92-a999-281572c1ead4 | -9.57232 | -64.22312 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7053da1e-99bc-3c72-9c28-40efe902e838 | -9.57177 | -64.22662 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6028fe7c-d2b3-3bae-9fed-32b54b2cefc5 | -9.56955 | -64.21909 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 208c3680-d4e8-3c65-91d5-d094d3e3d453 | -9.56845 | -64.22609 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d504e6f-b11e-3d8d-b9ab-ca933f6910f4 | -9.56622 | -64.21857 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf287a53-a0d3-32e4-9209-37c9892b1071 | -9.43425 | -64.28394 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0ebb6a-a5b7-3c35-bd03-154a9d75cd4d | -9.42172 | -63.6573 | 2024-10-06 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c0f33c-4447-39be-bee0-c4971e50a91b | -9.42117 | -63.6608 | 2024-10-06 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c99bc18-0564-3999-953f-04b67758bd39 | -9.41872 | -63.68905 | 2024-10-06 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f62de0b-b927-3f89-8deb-f899f7fa517f | -9.41226 | -63.65221 | 2024-10-06 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad8196bd-d25a-3aa1-ba33-655251c81f00 | -9.39865 | -63.51984 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ce37c9c-dc68-3eec-9d45-c6cbc3022e30 | -9.37958 | -63.70835 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 310a54d3-818f-3e19-ac8d-e3a6f13bd35e | -9.37903 | -63.71187 | 2024-10-06 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d372ccca-9077-300e-ba9c-024dcc024925 | -11.88603 | -63.28999 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d9a1418-c5f2-3223-8a3a-63098f48f08a | -11.87242 | -63.28787 | 2024-10-06 05:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df56be88-d451-35cc-9be1-3a5e71717cdb | -11.00586 | -63.90559 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35211f3d-3292-3b1a-8a5c-cf2d2a3145e4 | -10.99862 | -63.90808 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 78d12ffa-e789-36af-a7dd-855717143f0f | -10.99807 | -63.91162 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08de8a15-352f-39c0-ad49-148ab4ac3d9d | -10.99529 | -63.90752 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c162fee0-2006-385f-8dc9-ba378e331d04 | -10.99473 | -63.91108 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b0926f1-f840-32e1-8946-040d8597765d | -10.99418 | -63.91462 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e209aba3-adb3-38ca-b0c1-51cbfa9fbfb5 | -10.99308 | -63.92171 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f361750-186d-3bc9-9dad-909f664b77cf | -10.99253 | -63.92526 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f488c75d-f85e-3e7d-adc8-6731e002c26b | -10.98255 | -63.94545 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbbff487-699b-3278-b255-c30dc5250d32 | -10.98199 | -63.94901 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424ff26c-90ee-3852-acdf-2461559c891e | -10.98093 | -63.97785 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdc8a3ac-d1f7-37aa-85cb-d0603d8df086 | -10.97759 | -63.97734 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42650caa-55e4-34b5-a687-f54d75787fe4 | -10.97425 | -63.97682 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50358b8e-263c-357d-a922-3cc9b1f2f4c5 | -10.91953 | -63.88829 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7f1397a-3bfa-3736-9375-e3bc8eae1bdd | -10.91673 | -63.88427 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32407c1e-be6d-3012-b2cc-e811645d5ebc | -10.91619 | -63.88781 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 956a3ee8-f4b1-3c52-9f17-c67d8da1817e | -10.91564 | -63.89132 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63487ffe-ff29-3515-8309-eeadf57ee9d1 | -10.91277 | -63.86563 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11408175-f9f0-3a60-95c4-fb7d0e53d5f2 | -10.89708 | -63.91074 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ebae9f-f2b3-3248-98b4-97f0e496c587 | -10.89373 | -63.91024 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1c945cd-22a1-37ee-895c-25d5d49bac2b | -10.88426 | -63.90513 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README135.md)
