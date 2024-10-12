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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37bdfd9f-6151-3827-b580-bb34417ac1ae | -6.34723 | -58.17743 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11660024-5dd0-3fe9-a486-73463025199d | -6.3471 | -58.17054 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e2b270-27f0-365a-a60e-b16ef96a068b | -6.34665 | -58.18124 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91648ee9-3dcf-3b75-adc3-02de972212d9 | -6.34651 | -58.17435 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a41c427-1606-3524-b84f-98b9441a2271 | -6.34608 | -58.18507 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1ff6c5a-dd79-3241-ba87-ec82bdccdda5 | -6.34592 | -58.17817 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9df4709a-b8ea-3f9a-a0a5-55fbf9b53f5a | -6.34532 | -58.18198 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f89f86-7efa-3ef4-8bb4-e47e83f77ea5 | -6.34303 | -58.17382 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd3fb6f8-65b7-3a85-ba9e-ef9f78f8c398 | -6.34244 | -58.17763 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57204d3b-16ec-35e1-a2e1-93ac04fd6628 | -6.34185 | -58.18143 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94def633-8306-39f3-a087-61f224fa960e | -6.33583 | -58.3232 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66a36ff1-dde7-30ce-91ef-b1ba7b513853 | -6.33237 | -58.32267 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 966ced50-ad65-3160-a32c-7b986826f78a | -6.20531 | -57.78024 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffe5e49c-5b52-362e-9025-622fa908e830 | -6.20179 | -57.77972 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 730b8931-1c5a-314b-b6c3-6afbc7da653c | -6.19826 | -57.77918 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ccf2696-605d-37f5-9ebc-f0acaa910080 | -5.96962 | -57.67508 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 940c36da-b421-3b8c-9905-e1aae8f1a13d | -5.96012 | -57.68985 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 544dbe91-71c7-3953-9487-1375834a6718 | -5.95951 | -57.69384 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6de62aa-e075-39f4-afb4-9411c83fd5bd | -5.95658 | -57.68932 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a4501c-5c42-3b1f-8b0d-b53b579c783c | -5.95597 | -57.69333 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a58b78e-88ba-37ec-bf45-8237196bbbb6 | -5.94003 | -57.70304 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffb3790-ee23-33f3-8a6f-ce829fa2903f | -5.93942 | -57.70702 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dd11a75-f02a-3be0-ac82-ed7099f29063 | -5.93528 | -57.71045 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efc12bea-2e56-3ed3-9035-5984c46efe70 | -5.84934 | -57.70578 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0171004a-2834-3d7e-b109-8bebaa87245b | -5.84582 | -57.70526 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c20353b-207a-3d1c-b1db-7f4b35c4fd97 | -5.83999 | -57.6962 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bcdd18d-bade-34a8-a23f-e59a38af1e43 | -5.83939 | -57.70013 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1efc1186-d66a-3058-9f8f-effa3ae60393 | -5.83707 | -57.69168 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34aee4fd-e697-3368-b5b6-1a61c7cc661f | -5.83647 | -57.69561 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f19a662-a8b4-3a24-8fab-0c77d8b278e5 | -5.83586 | -57.69956 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb99d89-7942-3673-be18-8b55469b7a06 | -5.83354 | -57.69113 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68c8bc1d-1f8d-3c9a-b047-013e0fcbcf77 | -5.80576 | -57.73149 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de8fe95b-7fb3-37a2-8232-44bb998d9819 | -5.80224 | -57.73092 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad89659a-51f0-3b35-96b1-226c9b9baf45 | -5.80165 | -57.73482 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ec7535-17a1-339f-8417-e4a04fddeda9 | -6.82303 | -57.84175 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9802ec6c-c5f0-35f5-a510-e17eff3f571d | -6.8195 | -57.84122 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fad254e-52b0-3a61-8c32-f0514682b982 | -6.67491 | -58.7774 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a045d0bc-86b4-323d-abb7-a0a3653105c1 | -6.67434 | -58.78107 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e12cf949-9da9-382d-ae11-08c62456cf35 | -6.6715 | -58.77687 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94855a43-cd56-33d2-9d75-0a67f45ea085 | -6.67093 | -58.78054 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f5eac72-a965-31b9-a6b6-81b00116fa69 | -6.52747 | -58.40205 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daf215cb-d92c-3b10-a87f-4704ae106f1d | -6.52402 | -58.40154 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8073997-4a36-3723-9486-e2ac9b554012 | -6.52343 | -58.40531 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e9174cb-dbea-390e-932a-8f8bd5263d52 | -6.51998 | -58.4048 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af019cac-0f2b-3a8d-bbc1-21959fa4a55c | -6.51653 | -58.40427 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c82e4276-99ba-3ee6-8a21-bfcf01b51886 | -6.48255 | -58.46442 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c782d5c-d555-32f2-92c8-059aa1dfc2eb | -6.96004 | -58.98437 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d63b7d-de43-326d-b41e-24e6a8470686 | -6.95608 | -58.98748 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21133094-3eb4-3a39-ac74-4fc54331d134 | -6.91033 | -59.03621 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a177222-3bc4-3782-ae7e-d2e32552d292 | -6.89454 | -59.04861 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b39d9dd-e9f5-3a19-8d60-037ad0e30e6a | -6.86693 | -59.07029 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26ecfd85-4091-34c4-bd2d-5eb8a6c1cc1f | -6.86471 | -59.08479 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0e46748-53a1-328c-9df4-581f18baa465 | -6.8641 | -59.06613 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e83ec818-cb39-37e7-93ad-b4ef82abb644 | -6.86354 | -59.06976 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ad900f5-4108-386a-aa08-6239a19fc0cf | -6.86133 | -59.08425 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dd6914c-f689-3801-9be2-cc8a2772746e | -6.86077 | -59.08788 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5322603a-6a21-3dc2-b3de-b30e4cdd94d1 | -6.85693 | -59.08767 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e131ecef-43f7-3139-a2e6-bbf8ebdbf05a | -6.85684 | -59.09096 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9128cb4-a63b-368b-9f89-278de5002f07 | -6.85637 | -59.09128 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed8907b3-5124-322f-bf3d-9a797723f7c1 | -6.8416 | -58.98522 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e351a73-9d88-32a0-919b-3eb74e3bee59 | -6.84104 | -58.98885 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 787eb8fb-64b9-38f5-b09a-38f3d6b62a29 | -6.81624 | -59.03698 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce9c1a06-4540-327b-b4fa-1a25d890ade9 | -6.81568 | -59.04058 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb53a5fc-2243-3c1f-86b8-938ece3d3589 | -7.44726 | -58.60713 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c26454a6-7c6e-31d2-a8c5-cf0105d3c2f5 | -6.91316 | -59.04038 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5278a8-9335-3704-ae38-43ba90ea3a87 | -6.90977 | -59.03984 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1208419-dacd-3c4f-90e2-d804d1cf6e66 | -6.89681 | -59.05638 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e9eaad-bcb2-3a73-ae76-51aac4bba87a | -6.89398 | -59.05223 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c2f5217-0251-3648-a2e1-cdb624ecd9ea | -6.89342 | -59.05586 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71f8d71b-16b0-382f-bccb-8c909ea2be6d | -6.86976 | -59.07444 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ea86fc4-0579-3bbc-8c56-102090bfb761 | -6.86921 | -59.07806 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 329686fe-27ae-37f4-be7f-8dd16d722559 | -6.86865 | -59.08169 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09380f50-853c-37f7-9bbb-3162fd9a3502 | -6.86749 | -59.06666 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d87ad9db-fb56-3728-b80e-d8c0494a17eb | -6.86582 | -59.07752 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f00ec71b-46fb-36c7-9709-fa70f44e0ba5 | -6.86527 | -59.08115 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2de1e233-b86f-3adf-9fd2-9cc97b7f6bbc | -6.86416 | -59.08841 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692cfdb4-49f8-3067-9c9e-86f975f5e234 | -6.86361 | -59.09202 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad70e84-d4d8-36f0-a3cd-bead29ca8fbc | -6.86022 | -59.09149 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0db9d0e-f9e3-3b76-b4ff-09b1e54abbde | -6.85739 | -59.08735 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0346f8dc-5773-3932-aa4e-03d44543896a | -6.83369 | -58.99143 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8276c488-aa29-35d1-847c-6b2b395dd87e | -6.82803 | -58.9831 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83714958-5605-3c2f-ab94-862f34ce296e | -6.8134 | -59.03285 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 989f275f-e239-30bb-97d2-b605ed67576a | -6.81229 | -59.04006 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3afdfa6-c670-3d61-80d9-f21d75dc50a1 | -6.76042 | -59.06165 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 566f28fc-bfb3-3b2f-8487-49757cd5f0a0 | -6.75703 | -59.06113 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b7e715a-152b-3195-bfb5-9d46bd0f5dc3 | -6.75318 | -58.87872 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e213f635-030b-36a2-a1e2-11d3327e7052 | -6.74977 | -58.87823 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0967d74d-17d9-3442-9c79-2ef29dd34081 | -6.7492 | -58.88191 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7652562e-09d9-38de-9e7a-8b61e47fbfcf | -6.74637 | -58.87774 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df56a91b-7526-393c-8f66-634f37374444 | -6.7458 | -58.88143 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a934a57b-552a-3f58-ac03-9995ebc6865c | -6.74353 | -58.87355 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b51b2bf-5d2a-38f9-a13f-2438868cb53c | -6.74296 | -58.87721 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ad86be-fc53-37fb-8304-879d3ef0a669 | -6.7424 | -58.88087 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33154692-990b-3e19-91d8-87d31d5fd5fa | -6.71971 | -58.86991 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d912cba-4677-321f-ab19-0490679ac2fe | -6.71686 | -58.86573 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3633440-b984-31f6-8193-b52e2ac7ce93 | -9.22174 | -58.28287 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4677b8f3-8d63-31ca-8b84-c4c21614d992 | -9.21818 | -58.28234 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2fd49c-f370-3736-a592-62a129a33c59 | -9.21757 | -58.28635 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd6c2c4-1e2b-3f86-86b1-2bad4bd577b7 | -9.21697 | -58.29035 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c335864d-8d82-35ca-bf54-cc638a1545e3 | -9.21402 | -58.2858 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README105.md)
