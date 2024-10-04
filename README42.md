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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc4835c-734d-36bb-ae66-e1abeea4e071 | -21.7981 | -48.3926 | 2024-10-04 02:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3e8f1a63-82f4-3a8e-bc7a-bdb5f979969d | -21.7988 | -48.3691 | 2024-10-04 02:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 97671b34-5e20-3d9e-9f64-0660f85a6239 | -21.8196 | -48.3641 | 2024-10-04 02:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3d03c82b-3f86-3e28-8ae9-e7c4c1c847e1 | -22.2684 | -51.4941 | 2024-10-04 02:07:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| 72f2c829-700a-3987-864f-6cfa6c810d2b | -22.269 | -51.4714 | 2024-10-04 02:07:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.4 |
| c893c3fa-1763-3df0-966b-f5bf0cf42e16 | -3.2534 | -50.3689 | 2024-10-04 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 540de0cf-b21b-3c46-a2a0-a8eafb8207bb | -3.404 | -42.2858 | 2024-10-04 02:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2605ddd8-ceff-3424-8f08-22e5fb377fda | -3.2899 | -50.4725 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 036f22f9-472c-3a3d-8308-152f0cbb32aa | -3.2899 | -50.4516 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 264.1 |
| a65c37c0-0254-33cf-8521-fb256b21829a | -3.29 | -50.4306 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| ea3725a9-0204-3846-81c1-1711b2586cd3 | -3.3083 | -50.4719 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| aef478c0-56c2-3d17-a697-f21e0d96c286 | -3.3084 | -50.451 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 98ed487b-2df4-3f38-b723-ba44130bd906 | -3.3085 | -50.43 | 2024-10-04 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 95198844-31fe-37f7-a4d4-1e9a7f0c5055 | -4.0949 | -48.4894 | 2024-10-04 02:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 060adf88-2084-330d-8804-32c9c916d713 | -4.5375 | -43.304 | 2024-10-04 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e5af8097-945b-33a5-9520-343fdbcf4eca | -4.6684 | -45.8961 | 2024-10-04 02:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| cc52f9e3-3732-3400-a087-0fbe97939ff8 | -4.6686 | -45.8738 | 2024-10-04 02:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 256.3 |
| d78fdcbb-bde0-3355-98ca-d98199df145c | -4.687 | -45.8951 | 2024-10-04 02:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 267.1 |
| 88cf7a7f-0c1c-3ba2-9453-3aabe173c28b | -4.6872 | -45.8727 | 2024-10-04 02:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 524.8 |
| e4d5d830-f685-3756-9fe3-055daea43ebe | -4.6873 | -45.8504 | 2024-10-04 02:15:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3cad2e4a-94fd-3b91-a72d-11fdbd5bea4d | -4.7058 | -45.8717 | 2024-10-04 02:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fb7a7ed9-b258-387e-ac7f-e1c8bc545f90 | -5.8216 | -44.1196 | 2024-10-04 02:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 981e0bfc-03a9-3f9d-998f-5a2332597639 | -7.0529 | -71.7726 | 2024-10-04 02:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 9c515a07-a1d6-3eea-9474-2fb641c3373c | -7.0529 | -71.7544 | 2024-10-04 02:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| a4965bb3-1137-35cc-8146-f0d08ccd0818 | -7.0712 | -71.7542 | 2024-10-04 02:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f78c11b4-32ba-3f88-a58a-81c538dcfca1 | -7.8539 | -45.3611 | 2024-10-04 02:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 06f6f6c6-7f45-3b7b-8c46-f90887be074d | -7.8164 | -50.543 | 2024-10-04 02:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7f423f96-1916-390f-a0e3-23f10bd88941 | -7.8166 | -50.5219 | 2024-10-04 02:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 04194743-9a65-3ca1-bede-9672732ef743 | -7.8351 | -50.5416 | 2024-10-04 02:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| ee5248e9-8533-326b-8a34-53579960095f | -7.8353 | -50.5204 | 2024-10-04 02:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| d3c66486-320c-3015-9623-4bca609bfbb3 | -8.6448 | -50.0518 | 2024-10-04 02:15:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 3e0a975d-3f9e-30ef-9275-c008c2d19f09 | -8.6636 | -50.0501 | 2024-10-04 02:15:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 12973fad-527f-32cc-93cb-c5038db4a9e0 | -9.0853 | -50.9036 | 2024-10-04 02:15:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7eab82d4-e51b-3644-982f-524142130399 | -9.1041 | -50.902 | 2024-10-04 02:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 80ff7e1e-6bc2-3b9c-94a7-77449c85f192 | -9.0162 | -67.3904 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b62446cc-1bbc-397a-899c-7ad19e8df1f1 | -9.0347 | -67.39 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ae2a2aff-b3ad-3899-be46-ea109da641a7 | -9.0898 | -67.5183 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 973f07c7-6b4e-33f8-a31b-e3093bce13a5 | -9.0898 | -67.4997 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 721f1b53-2e84-35f6-916b-b4e590454152 | -9.0899 | -67.4812 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 01e967a3-d339-39f2-b493-e9294e0985bb | -9.1084 | -67.4993 | 2024-10-04 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fdcc4fbc-d469-334b-9cd4-66792706d739 | -9.3115 | -50.8203 | 2024-10-04 02:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 6db85710-c32a-3410-91ff-5ce8ee2bfbb7 | -9.3118 | -50.7991 | 2024-10-04 02:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| def3dff1-c7c9-3d4b-99f6-ffb10999cc91 | -9.3303 | -50.8186 | 2024-10-04 02:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| ca9fedf7-ed69-3e0a-b8aa-daed33949113 | -9.3306 | -50.7974 | 2024-10-04 02:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 365fb4c5-c656-3adc-8ca7-e289e769adc9 | -9.8353 | -46.7502 | 2024-10-04 02:16:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4d4fec1f-926b-3b75-9515-30c295f56b84 | -9.7684 | -51.9139 | 2024-10-04 02:16:01 | GOES-16 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 23d242ea-ced2-3331-83bf-59d742be82a6 | -9.7873 | -51.9122 | 2024-10-04 02:16:02 | GOES-16 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ac5db8ac-99a1-3303-81ca-a027fda00215 | -9.8247 | -51.9297 | 2024-10-04 02:16:02 | GOES-16 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 6d8a3a97-1ea8-360c-b84e-a3c68c4c7a1f | -10.8661 | -46.3331 | 2024-10-04 02:16:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 24c4fc24-5082-3c99-a815-1c790a165929 | -11.0918 | -46.5069 | 2024-10-04 02:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a4db08b2-5f64-3f8d-b100-d2fc440f0835 | -11.0921 | -46.4843 | 2024-10-04 02:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 95b64f7e-362d-3711-bfd4-dd1f6c515e7e | -11.1112 | -46.4818 | 2024-10-04 02:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 49b66b86-7bdc-3006-b199-c5df3987a738 | -11.7618 | -58.8894 | 2024-10-04 02:16:13 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a37e50f4-f657-3875-82cf-3ed8c69b59be | -11.8242 | -56.6009 | 2024-10-04 02:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c1b60347-bae9-36b6-a880-056bc35dfd7c | -12.5898 | -53.1359 | 2024-10-04 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ee96f7a5-1411-3454-8e9b-92ac7b81626f | -12.5901 | -53.115 | 2024-10-04 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 163.8 |
| fd2ec6f5-9c40-3657-9415-d4c543a8e798 | -12.6092 | -53.1129 | 2024-10-04 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 1ae6fdc0-275e-324a-b9d1-a1ea4a1656bb | -12.6296 | -63.1033 | 2024-10-04 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b923a29d-a211-3089-a531-94d7936490a9 | -12.6295 | -63.1225 | 2024-10-04 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f7118825-86b5-33b6-a4ad-e57f866bb027 | -14.7939 | -48.0275 | 2024-10-04 02:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 64348be4-38c5-3b35-95e5-6d04f4c5cc17 | -16.0732 | -50.3014 | 2024-10-04 02:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 23f1b524-763b-30e1-813a-48d7b50fef40 | -16.0737 | -50.2794 | 2024-10-04 02:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1dd11fe3-a5ac-3950-88b1-de94f4a33c2a | -16.0929 | -50.2983 | 2024-10-04 02:16:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a888d5cf-3e74-3c7b-a3f3-e55ca4a37f52 | -16.0933 | -50.2763 | 2024-10-04 02:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 31cfdcba-c85b-3f0c-96bb-229bf19f9e1a | -16.5938 | -57.1783 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| de35f89c-ede0-3dcd-894f-82faf61228fd | -16.5935 | -57.1988 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 361825b5-e66d-309a-8eac-9925f2b252c8 | -16.5928 | -57.2397 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| e54acb83-9237-3f5c-94ce-ebb183658ca5 | -16.5925 | -57.2602 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 190e02ef-e42c-302d-a85d-5b90e63dec4a | -16.5736 | -57.2215 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| c968e9d0-f571-384f-adf2-123f8b87f41b | -16.5733 | -57.2419 | 2024-10-04 02:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| fd58be6f-02a3-36fe-8735-a30bf7edcc44 | -16.4151 | -57.3823 | 2024-10-04 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 3c405a7e-9a17-39ba-8ed1-fec3fcca866e | -16.4148 | -57.4028 | 2024-10-04 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 990e6574-495b-33e3-902f-972ee0dc1148 | -16.765 | -57.4652 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 100ade1e-b62e-316b-b4d5-8f6ed5d7c7bb | -16.7259 | -57.4696 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 6468a90e-2655-3efb-8169-02aa5e766763 | -16.7455 | -57.4674 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 90f974be-64c8-39cb-8591-b7687cd00141 | -16.7606 | -57.7512 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| d3d72742-2ee6-3c3c-b264-98cfe6f5e358 | -16.7647 | -57.4856 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 1749d5a4-c218-329a-b401-880ea90c2037 | -16.6871 | -57.4536 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 45927ac2-65d2-3114-83e3-706586988995 | -16.6868 | -57.4741 | 2024-10-04 02:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| cf474aaa-1b16-3b79-98d7-95e576efda87 | -16.6133 | -57.176 | 2024-10-04 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| 4726b2cf-a2b2-3a70-85b0-f9512f228472 | -16.613 | -57.1965 | 2024-10-04 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| ff288b55-64ca-36d4-887b-614c5893e515 | -16.9287 | -55.8197 | 2024-10-04 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 8c135689-4d63-3d3b-a386-b33485c3dfa7 | -16.9283 | -55.8405 | 2024-10-04 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| d619c1f9-c44e-3646-8a60-ec3882ed46c1 | -16.9087 | -55.843 | 2024-10-04 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| bbb3ff1f-ca12-3133-8539-6400f2c6e83a | -16.843 | -57.4767 | 2024-10-04 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 71706397-9dda-3daa-a64d-3abb6771094d | -16.8055 | -57.3788 | 2024-10-04 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 79a7480d-dc59-37cb-802e-588e63173ddb | -16.7859 | -57.3811 | 2024-10-04 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 11a8e8e1-fa8d-3645-9fb9-524f0e1931a6 | -16.7843 | -57.4834 | 2024-10-04 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| b0175879-0670-36a4-ab89-2aed57f30e3b | -17.0512 | -56.6932 | 2024-10-04 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 985ccdd9-ad11-35ab-8eee-f43a42ed61f7 | -17.3844 | -42.6235 | 2024-10-04 02:16:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ca85c4b6-dc5a-374e-9c2f-374dbd29ca55 | -17.1774 | -57.3764 | 2024-10-04 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 791920fa-aaa0-3c4a-be69-13ff97a07a60 | -17.1771 | -57.3969 | 2024-10-04 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.8 |
| e0894f6f-e9c3-35e9-ba83-12218e3339b8 | -17.1577 | -57.3787 | 2024-10-04 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 0310458a-4558-305e-899c-ace7145c2beb | -17.1574 | -57.3993 | 2024-10-04 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.4 |
| debcd80c-4da8-3ab5-b660-917adbcf7f6d | -17.5344 | -46.7239 | 2024-10-04 02:16:43 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f2ad8c17-00a0-31dc-95f0-5bc1894d6368 | -17.7307 | -43.8127 | 2024-10-04 02:16:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 138680d1-494f-3738-b64d-ac34bab54111 | -17.7508 | -43.8079 | 2024-10-04 02:16:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 902bfeb3-bf78-3cc0-aa07-935dd063226d | -18.8613 | -43.5837 | 2024-10-04 02:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| e51b796f-18df-3440-874f-73daba140121 | -19.3159 | -42.5976 | 2024-10-04 02:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 67574e75-4ae5-3371-80f2-4471d1608525 | -19.3167 | -42.5724 | 2024-10-04 02:16:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |


[Clique aqui para ver as próximas entradas](README43.md)
